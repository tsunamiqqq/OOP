import tkinter as tk
import random

all_grids = []

class TSG(tk.Frame):
    def __init__(self, master=None, rows=4, cols=5):
        super().__init__(master)
        self.rows = rows
        self.cols = cols
        self.cells = []
        self.flag = True
        
        for r in range(rows):
            row_cells = []
            for c in range(cols):
                cell = tk.Entry(self, width=8, font=("Arial", 10), justify='center')
                cell.grid(row=r, column=c, padx=1, pady=1)
                cell.bind("<Button-1>", self.on_click) 
                row_cells.append(cell)
            self.cells.append(row_cells)

    def fill_random(self):
        for r in range(self.rows):
            for c in range(self.cols):
                self.cells[r][c].delete(0, tk.END)
                self.cells[r][c].insert(0, str(random.randint(0, 20)))

    def clear_cells(self):
        for r in range(self.rows):
            for c in range(self.cols):
                self.cells[r][c].delete(0, tk.END)

    def on_click(self, event):
        new_size = 20 if self.flag else 10
        for r in range(self.rows):
            for c in range(self.cols):
                self.cells[r][c].config(font=("Arial", new_size))
        self.flag = not self.flag

def run_task_2():
    root = tk.Tk()
    root.title("Власний компонент")
    root.geometry("500x300")
    fill_index = [0] 

    def show_component():
        sg_t = TSG(root, rows=4, cols=5)
        sg_t.pack(pady=10)
        all_grids.append(sg_t)

    def handle_f11(event):
        if fill_index[0] < len(all_grids):
            all_grids[fill_index[0]].fill_random()
            fill_index[0] += 1
        else:
            print("Всі існуючі компоненти вже заповнені")

    def handle_esc(event):
        if fill_index[0] > 0:
            fill_index[0] -= 1
            all_grids[fill_index[0]].clear_cells()
        else:
            print("Немає заповнених компонентів для очищення")

    btn = tk.Button(root, text="Відобразити компонент", command=show_component)
    btn.pack(pady=10)

    root.bind("<F11>", handle_f11)
    root.bind("<Escape>", handle_esc)

    root.mainloop()

if __name__ == "__main__":
    run_task_2()
