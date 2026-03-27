import tkinter as tk
from tkinter import ttk, messagebox
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    quantity: int
    price: float

class Notebook:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, index):
        if 0 <= index < len(self.items):
            del self.items[index]
        else:
            raise IndexError("Невірний індекс")

    def get_all_items(self):
        return self.items

    def clear_all(self):
        self.items.clear()

    def __del__(self):
        pass

class Journal(Notebook):
    def __init__(self):
        super().__init__()

    def total_quantity(self):
        return sum(item.quantity for item in self.items)

    def find_by_name(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Журнал обліку продукції на складі")
        self.root.geometry("750x500")
        self.root.resizable(False, False)

        self.journal = Journal()

        input_frame = tk.LabelFrame(root, text="Дані про товар", padx=10, pady=10)
        input_frame.pack(fill="x", padx=10, pady=10)

        tk.Label(input_frame, text="Назва товару:").grid(row=0, column=0, sticky="w")
        self.name_entry = tk.Entry(input_frame, width=25)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Кількість:").grid(row=0, column=2, sticky="w")
        self.quantity_entry = tk.Entry(input_frame, width=15)
        self.quantity_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(input_frame, text="Ціна:").grid(row=0, column=4, sticky="w")
        self.price_entry = tk.Entry(input_frame, width=15)
        self.price_entry.grid(row=0, column=5, padx=5, pady=5)

        button_frame = tk.Frame(root)
        button_frame.pack(fill="x", padx=10, pady=5)

        tk.Button(button_frame, text="Додати товар", width=18, command=self.add_product).pack(side="left", padx=5)
        tk.Button(button_frame, text="Видалити товар", width=18, command=self.delete_product).pack(side="left", padx=5)
        tk.Button(button_frame, text="Знайти товар", width=18, command=self.find_product).pack(side="left", padx=5)
        tk.Button(button_frame, text="Очистити все", width=18, command=self.clear_all).pack(side="left", padx=5)

        table_frame = tk.Frame(root)
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        columns = ("name", "quantity", "price")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
        self.tree.heading("name", text="Назва товару")
        self.tree.heading("quantity", text="Кількість")
        self.tree.heading("price", text="Ціна")

        self.tree.column("name", width=300)
        self.tree.column("quantity", width=150, anchor="center")
        self.tree.column("price", width=150, anchor="center")

        self.tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        self.info_label = tk.Label(root, text="Загальна кількість товарів: 0", font=("Arial", 11, "bold"))
        self.info_label.pack(pady=5)

    def add_product(self):
        name = self.name_entry.get().strip()
        quantity = self.quantity_entry.get().strip()
        price = self.price_entry.get().strip()

        if not name or not quantity or not price:
            messagebox.showwarning("Попередження", "Заповніть усі поля.")
            return

        try:
            quantity = int(quantity)
            price = float(price)
        except ValueError:
            messagebox.showerror("Помилка", "Кількість повинна бути цілим числом, а ціна — числом.")
            return

        product = Product(name, quantity, price)
        self.journal.add_item(product)
        self.update_table()
        self.clear_entries()

    def delete_product(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Попередження", "Оберіть товар для видалення.")
            return

        item_index = self.tree.index(selected[0])
        self.journal.remove_item(item_index)
        self.update_table()

    def find_product(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("Попередження", "Введіть назву товару для пошуку.")
            return

        product = self.journal.find_by_name(name)
        if product:
            messagebox.showinfo(
                "Товар знайдено",
                f"Назва: {product.name}\nКількість: {product.quantity}\nЦіна: {product.price:.2f}"
            )
        else:
            messagebox.showinfo("Результат", "Товар не знайдено.")

    def clear_all(self):
        self.journal.clear_all()
        self.update_table()

    def update_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for item in self.journal.get_all_items():
            self.tree.insert("", "end", values=(item.name, item.quantity, f"{item.price:.2f}"))

        self.info_label.config(
            text=f"Загальна кількість товарів: {self.journal.total_quantity()}"
        )

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
