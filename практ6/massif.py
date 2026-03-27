import tkinter as tk
from tkinter import ttk, messagebox
import copy


class SparseElement:
    def __init__(self, logical_index, value=None):
        self.logical_index = logical_index
        self.value = value

    def __str__(self):
        return f"Індекс: {self.logical_index}, Значення: {self.value}"


class SparseArray:
    def __init__(self, logical_size=10):
        self.logical_size = logical_size
        self.data = []

    def copy(self):
        new_array = SparseArray(self.logical_size)
        new_array.data = [SparseElement(el.logical_index, copy.deepcopy(el.value)) for el in self.data]
        return new_array

    def assign(self, other):
        if self is not other:
            self.logical_size = other.logical_size
            self.data = [SparseElement(el.logical_index, copy.deepcopy(el.value)) for el in other.data]

    def get_element(self, index):
        if index < 0 or index >= self.logical_size:
            raise IndexError("Індекс поза межами логічного масиву")

        for element in self.data:
            if element.logical_index == index:
                return element

        new_element = SparseElement(index, 0)
        self.data.append(new_element)
        self.data.sort(key=lambda x: x.logical_index)
        return new_element

    def set_value(self, index, value):
        element = self.get_element(index)
        element.value = value

    def get_value(self, index):
        element = self.get_element(index)
        return element.value

    def delete_value(self, index):
        for i, element in enumerate(self.data):
            if element.logical_index == index:
                del self.data[i]
                return True
        return False

    def show(self):
        if not self.data:
            return "Фізичний масив порожній"
        return "\n".join(str(element) for element in self.data)


class SparseArrayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Розріджений одновимірний масив")
        self.root.geometry("760x600")
        self.root.resizable(False, False)

        self.sparse_array = SparseArray(10)
        self.copied_array = None

        self.create_widgets()
        self.update_output()

    def create_widgets(self):
        title = tk.Label(
            self.root,
            text="Лабораторна робота: Розріджений одновимірний масив",
            font=("Arial", 14, "bold")
        )
        title.pack(pady=10)

        frame_size = ttk.LabelFrame(self.root, text="Налаштування масиву")
        frame_size.pack(fill="x", padx=10, pady=5)

        tk.Label(frame_size, text="Логічний розмір:").grid(row=0, column=0, padx=5, pady=5)
        self.size_entry = tk.Entry(frame_size, width=15)
        self.size_entry.grid(row=0, column=1, padx=5, pady=5)
        self.size_entry.insert(0, "10")

        tk.Button(frame_size, text="Створити масив", command=self.create_array).grid(
            row=0, column=2, padx=5, pady=5
        )

        frame_actions = ttk.LabelFrame(self.root, text="Операції")
        frame_actions.pack(fill="x", padx=10, pady=5)

        tk.Label(frame_actions, text="Індекс:").grid(row=0, column=0, padx=5, pady=5)
        self.index_entry = tk.Entry(frame_actions, width=10)
        self.index_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_actions, text="Значення:").grid(row=0, column=2, padx=5, pady=5)
        self.value_entry = tk.Entry(frame_actions, width=15)
        self.value_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Button(frame_actions, text="Додати / змінити", command=self.set_value).grid(
            row=0, column=4, padx=5, pady=5
        )
        tk.Button(frame_actions, text="Отримати", command=self.get_value).grid(
            row=0, column=5, padx=5, pady=5
        )
        tk.Button(frame_actions, text="Видалити", command=self.delete_value).grid(
            row=0, column=6, padx=5, pady=5
        )

        frame_copy = ttk.LabelFrame(self.root, text="Копіювання і присвоєння")
        frame_copy.pack(fill="x", padx=10, pady=5)

        tk.Button(frame_copy, text="Копія масиву", command=self.copy_array).grid(
            row=0, column=0, padx=5, pady=5
        )
        tk.Button(frame_copy, text="Присвоїти копію назад", command=self.assign_array).grid(
            row=0, column=1, padx=5, pady=5
        )

        frame_demo = ttk.LabelFrame(self.root, text="Демонстрація")
        frame_demo.pack(fill="x", padx=10, pady=5)

        tk.Button(frame_demo, text="Заповнити прикладом", command=self.fill_demo).grid(
            row=0, column=0, padx=5, pady=5
        )
        tk.Button(frame_demo, text="Очистити", command=self.clear_array).grid(
            row=0, column=1, padx=5, pady=5
        )

        frame_output = ttk.LabelFrame(self.root, text="Вміст фізичного масиву")
        frame_output.pack(fill="both", expand=True, padx=10, pady=10)

        self.output_text = tk.Text(frame_output, width=85, height=20, font=("Consolas", 11))
        self.output_text.pack(padx=5, pady=5)

    def create_array(self):
        try:
            size = int(self.size_entry.get())
            if size <= 0:
                raise ValueError
            self.sparse_array = SparseArray(size)
            self.copied_array = None
            self.update_output()
            messagebox.showinfo("Успіх", f"Створено масив логічного розміру {size}")
        except ValueError:
            messagebox.showerror("Помилка", "Введіть коректний додатний розмір")

    def set_value(self):
        try:
            index = int(self.index_entry.get())
            value_text = self.value_entry.get().strip()

            if value_text == "":
                messagebox.showerror("Помилка", "Введіть значення")
                return

            try:
                if "." in value_text:
                    value = float(value_text)
                else:
                    value = int(value_text)
            except ValueError:
                value = value_text

            self.sparse_array.set_value(index, value)
            self.update_output()
            messagebox.showinfo("Успіх", f"Елемент з індексом {index} додано/змінено")
        except ValueError:
            messagebox.showerror("Помилка", "Індекс має бути цілим числом")
        except IndexError as e:
            messagebox.showerror("Помилка", str(e))

    def get_value(self):
        try:
            index = int(self.index_entry.get())
            value = self.sparse_array.get_value(index)
            self.update_output()
            messagebox.showinfo("Значення", f"Елемент [{index}] = {value}")
        except ValueError:
            messagebox.showerror("Помилка", "Індекс має бути цілим числом")
        except IndexError as e:
            messagebox.showerror("Помилка", str(e))

    def delete_value(self):
        try:
            index = int(self.index_entry.get())
            deleted = self.sparse_array.delete_value(index)
            self.update_output()
            if deleted:
                messagebox.showinfo("Успіх", f"Елемент з індексом {index} видалено")
            else:
                messagebox.showwarning("Увага", f"Елемент з індексом {index} не знайдено")
        except ValueError:
            messagebox.showerror("Помилка", "Індекс має бути цілим числом")

    def copy_array(self):
        self.copied_array = self.sparse_array.copy()
        messagebox.showinfo("Копіювання", "Створено копію масиву")

    def assign_array(self):
        if self.copied_array is None:
            messagebox.showwarning("Увага", "Спочатку створіть копію масиву")
            return
        self.sparse_array.assign(self.copied_array)
        self.update_output()
        messagebox.showinfo("Присвоєння", "Копію присвоєно поточному масиву")

    def fill_demo(self):
        self.sparse_array = SparseArray(15)
        self.sparse_array.set_value(1, 100)
        self.sparse_array.set_value(4, 3.14)
        self.sparse_array.set_value(7, "Python")
        self.sparse_array.set_value(10, 500)
        self.update_output()
        messagebox.showinfo("Демонстрація", "Масив заповнено тестовими значеннями")

    def clear_array(self):
        size = self.sparse_array.logical_size
        self.sparse_array = SparseArray(size)
        self.update_output()
        messagebox.showinfo("Очищення", "Масив очищено")

    def update_output(self):
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, f"Логічний розмір масиву: {self.sparse_array.logical_size}\n")
        self.output_text.insert(tk.END, "-" * 60 + "\n")
        self.output_text.insert(tk.END, self.sparse_array.show())


if __name__ == "__main__":
    root = tk.Tk()
    app = SparseArrayApp(root)
    root.mainloop()
