import tkinter as tk

class BtnNClick(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.n_click = 0  
        self.config(text=f"Кнопка натискань", command=self.handle_click)

    def handle_click(self):
        self.n_click += 1
        self.config(text=f"Кнопка {self.n_click} натискань")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Кількість натискань")
    root.geometry("300x200")
    
    my_button = BtnNClick(root)
    my_button.pack(expand=True)
    
    root.mainloop()