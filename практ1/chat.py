import socket
import threading
import datetime
import tkinter as tk
from tkinter import messagebox, scrolledtext

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Чат")
        self.root.geometry("650x550")
        
        self.server_socket = None
        self.client_socket = None
        self.is_running = False
        self.clients = {} 

        self.setup_frame = tk.LabelFrame(root, text="Налаштування")
        self.setup_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(self.setup_frame, text="Нік:").grid(row=0, column=0, padx=5)
        self.ent_nick = tk.Entry(self.setup_frame, width=12)
        self.ent_nick.insert(0, "User")
        self.ent_nick.grid(row=0, column=1)

        tk.Label(self.setup_frame, text="IP:").grid(row=0, column=2, padx=5)
        self.ent_ip = tk.Entry(self.setup_frame, width=12)
        self.ent_ip.insert(0, "127.0.0.1")
        self.ent_ip.grid(row=0, column=3)

        tk.Label(self.setup_frame, text="Порт:").grid(row=0, column=4, padx=5)
        self.ent_port = tk.Entry(self.setup_frame, width=6)
        self.ent_port.insert(0, "5000")
        self.ent_port.grid(row=0, column=5)

        self.btn_main = tk.Button(self.setup_frame, text="Запустити сервер", bg="lightgreen", width=20, command=self.toggle_server)
        self.btn_main.grid(row=0, column=6, padx=10)

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(expand=True, fill="both", padx=10, pady=5)

        self.txt_log = scrolledtext.ScrolledText(self.main_frame, width=45, height=20)
        self.txt_log.pack(side="left", expand=True, fill="both")

        self.lst_users = tk.Listbox(self.main_frame, width=20)
        self.lst_users.pack(side="right", fill="y", padx=(5, 0))

        self.msg_frame = tk.Frame(root)
        self.msg_frame.pack(fill="x", padx=10, pady=5)

        self.ent_msg = tk.Entry(self.msg_frame)
        self.ent_msg.pack(side="left", expand=True, fill="x")
        self.ent_msg.bind("<Return>", lambda e: self.send_message())
        self.ent_msg.config(state="disabled")

        self.btn_send = tk.Button(self.msg_frame, text="Відправити", command=self.send_message, state="disabled")
        self.btn_send.pack(side="right", padx=5)

    def log(self, message):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        self.txt_log.config(state="normal")
        self.txt_log.insert(tk.END, f"[{now}] {message}\n")
        self.txt_log.see(tk.END)
        self.txt_log.config(state="disabled")

    def toggle_server(self):
        if not self.is_running:
            self.launch_master_mode()
        else:
            self.stop_network()

    def launch_master_mode(self):
        if self.start_server_logic():
            self.root.after(300, self.start_client_mode)

    def start_server_logic(self):
        try:
            port = int(self.ent_port.get())
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind(('', port))
            self.server_socket.listen(5)
            self.is_running = True
            self.log("Сервер запущений")
            
            self.btn_main.config(text="Відключитись", bg="orange")
            
            threading.Thread(target=self.server_accept_loop, daemon=True).start()
            return True
        except Exception as e:
            messagebox.showerror("Помилка", f"Помилка сервера: {str(e)}")
            return False

    def server_accept_loop(self):
        while self.is_running:
            try:
                conn, addr = self.server_socket.accept()
                threading.Thread(target=self.server_handle_client, args=(conn, addr), daemon=True).start()
            except: break

    def server_handle_client(self, conn, addr):
        nickname = ""
        try:
            data = conn.recv(1024).decode('utf-8')
            if data.startswith("#"):
                nickname = data[1:]
                self.clients[conn] = nickname
                self.update_user_list_ui()
                self.broadcast_user_list()
                self.log(f"{nickname} підключився")

            while self.is_running:
                msg = conn.recv(1024).decode('utf-8')
                if not msg: break
                if "~" in msg:
                    self.broadcast_to_all(msg, exclude_conn=conn)
                    parts = msg.split("~")
                    sender_name = parts[0].split("#")[1]
                    if sender_name != self.ent_nick.get():
                        self.log(f"{sender_name}: {parts[1]}")
        except: pass
        finally:
            if conn in self.clients:
                del self.clients[conn]
                self.update_user_list_ui()
                self.broadcast_user_list()
            conn.close()

    def broadcast_to_all(self, message, exclude_conn=None):
        for conn in list(self.clients.keys()):
            if conn != exclude_conn:
                try: conn.send(message.encode('utf-8'))
                except: pass

    def broadcast_user_list(self):
        user_list_msg = "#" + ",".join(self.clients.values())
        self.broadcast_to_all(user_list_msg)

    def update_user_list_ui(self):
        self.lst_users.delete(0, tk.END)
        for name in self.clients.values():
            self.lst_users.insert(tk.END, name)

    def start_client_mode(self):
        try:
            host = self.ent_ip.get()
            port = int(self.ent_port.get())
            nick = self.ent_nick.get()
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((host, port))
            self.client_socket.send(f"#{nick}".encode('utf-8'))
            self.is_running = True
            
            self.ent_msg.config(state="normal")
            self.btn_send.config(state="normal")
            threading.Thread(target=self.client_receive_loop, daemon=True).start()
        except Exception as e:
            messagebox.showerror("Помилка", f"Помилка клієнта: {str(e)}")

    def client_receive_loop(self):
        while self.is_running:
            try:
                data = self.client_socket.recv(1024).decode('utf-8')
                if not data: break
                if data.startswith("#"):
                    users = data[1:].split(",")
                    self.lst_users.delete(0, tk.END)
                    for u in users: self.lst_users.insert(tk.END, u)
                elif "~" in data:
                    parts = data.split("~")
                    sender_name = parts[0].split("#")[1]
                    if sender_name != self.ent_nick.get():
                        self.log(f"{sender_name}: {parts[1]}")
            except: break

    def send_message(self):
        msg_text = self.ent_msg.get()
        if msg_text and self.client_socket:
            nick = self.ent_nick.get()
            full_msg = f"All#{nick}~{msg_text}"
            try:
                self.client_socket.send(full_msg.encode('utf-8'))
                self.log(f"{nick}: {msg_text}") 
                self.ent_msg.delete(0, tk.END)
            except: self.log("Помилка відправки")

    def stop_network(self):
        self.is_running = False
        if self.client_socket:
            self.client_socket.close()
            self.client_socket = None
        if self.server_socket:
            self.server_socket.close()
            self.server_socket = None
        self.log("Сервер відключений")
        
        self.btn_main.config(text="Запустити сервер", bg="lightgreen")
        self.ent_msg.config(state="disabled")
        self.btn_send.config(state="disabled")
        self.lst_users.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
