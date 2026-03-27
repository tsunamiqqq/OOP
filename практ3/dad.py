import tkinter as tk
from tkinter import messagebox

def make_patronymic(father_name):
    name = father_name.strip()

    if not name:
        return ""

    lower_name = name.lower()

    if lower_name.endswith("й"):
        base = name[:-1]
        return base + "йович"

    if lower_name.endswith("а"):
        base = name[:-1]
        return base + "ович"

    if lower_name.endswith("ь"):
        base = name[:-1]
        return base + "ьович"

    if lower_name.endswith("о"):
        base = name[:-1]
        return base + "ович"
    if lower_name.endswith("с"):
        base = name[:-1]
        return base + "симович"

    return name + "ович"

class Father:
    def __init__(self, father_name):
        self.father_name = father_name

    def show_info(self):
        return f"Батько: {self.father_name}"

class Child(Father):
    def __init__(self, father_name, child_name):
        super().__init__(father_name)
        self.child_name = child_name
        self.patronymic = make_patronymic(father_name)

    def show_info(self):
        return f"Дитина: {self.child_name} {self.patronymic}"

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Батько та дитина")
        self.root.geometry("560x500")
        self.root.resizable(False, False)

        self.fathers = []
        self.children = []

        tk.Label(root, text="Ім'я батька:", font=("Arial", 12)).pack(pady=5)
        self.entry_father = tk.Entry(root, font=("Arial", 12), width=35)
        self.entry_father.pack()

        tk.Label(root, text="Ім'я дитини:", font=("Arial", 12)).pack(pady=5)
        self.entry_child = tk.Entry(root, font=("Arial", 12), width=35)
        self.entry_child.pack()

        tk.Button(
            root,
            text="Додати батька і дитину",
            font=("Arial", 11),
            command=self.add_family
        ).pack(pady=10)

        tk.Button(
            root,
            text="Очистити",
            font=("Arial", 11),
            command=self.clear_all
        ).pack(pady=5)

        tk.Label(root, text="Результат:", font=("Arial", 12, "bold")).pack(pady=8)

        self.text = tk.Text(root, width=64, height=18, font=("Arial", 11))
        self.text.pack(pady=5)

    def add_family(self):
        father_name = self.entry_father.get().strip()
        child_name = self.entry_child.get().strip()

        if not father_name or not child_name:
            messagebox.showerror("Помилка", "Введіть ім'я батька і ім'я дитини.")
            return

        father = Father(father_name)
        child = Child(father_name, child_name)

        self.fathers.append(father)
        self.children.append(child)

        self.show_all()

        self.entry_father.delete(0, tk.END)
        self.entry_child.delete(0, tk.END)

    def show_all(self):
        self.text.delete(1.0, tk.END)

        if not self.fathers and not self.children:
            self.text.insert(tk.END, "Список порожній.\n")
            return

        self.text.insert(tk.END, "Інформація про батьків і дітей:\n\n")

        count = min(len(self.fathers), len(self.children))
        for i in range(count):
            self.text.insert(tk.END, f"{i + 1}. {self.fathers[i].show_info()}\n")
            self.text.insert(tk.END, f"   {self.children[i].show_info()}\n\n")

    def clear_all(self):
        self.fathers.clear()
        self.children.clear()
        self.text.delete(1.0, tk.END)
        self.entry_father.delete(0, tk.END)
        self.entry_child.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
