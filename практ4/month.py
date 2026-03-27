import tkinter as tk
from tkinter import messagebox

months = {
    1: "Січень",
    2: "Лютий",
    3: "Березень",
    4: "Квітень",
    5: "Травень",
    6: "Червень",
    7: "Липень",
    8: "Серпень",
    9: "Вересень",
    10: "Жовтень",
    11: "Листопад",
    12: "Грудень"
}

def find_month():
    value = entry_number.get().strip()

    if not value:
        messagebox.showwarning("Введіть номер місяця.")
        return

    if not value.isdigit():
        messagebox.showerror("Потрібно ввести ціле число від 1 до 12.")
        return

    number = int(value)

    if number in months:
        result_label.config(text=f"Назва місяця: {months[number]}")
    else:
        result_label.config(text="Місяця з таким номером не існує.")

root = tk.Tk()
root.title("Назва місяца за номером")
root.geometry("400x180")
root.resizable(False, False)

title_label = tk.Label(root, text="Введіть номер місяця", font=("Arial", 14))
title_label.pack(pady=15)

entry_number = tk.Entry(root, font=("Arial", 14), justify="center")
entry_number.pack(pady=5)

find_button = tk.Button(root, text="Дізнатися назву місяця", font=("Arial", 12), command=find_month)
find_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 13), fg="blue")
result_label.pack(pady=5)

root.mainloop()
