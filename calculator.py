import tkinter as tk
from tkinter import messagebox

# Function
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            messagebox.showwarning("Warning", "Select an operation!")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers!")

# Main Window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("500x400")
root.configure(bg="#1E3A5F")

# Title
title = tk.Label(
    root,
    text="🧮 Simple Calculator",
    font=("Arial", 20, "bold"),
    bg="#1E3A5F",
    fg="white"
)
title.pack(pady=15)

# Number 1
tk.Label(
    root,
    text="Enter First Number",
    bg="#1E3A5F",
    fg="white",
    font=("Arial", 12)
).pack()

entry1 = tk.Entry(root, font=("Arial", 12))
entry1.pack(pady=5)

# Number 2
tk.Label(
    root,
    text="Enter Second Number",
    bg="#1E3A5F",
    fg="white",
    font=("Arial", 12)
).pack()

entry2 = tk.Entry(root, font=("Arial", 12))
entry2.pack(pady=5)

# Operation
operation_var = tk.StringVar()

tk.Label(
    root,
    text="Select Operation",
    bg="#1E3A5F",
    fg="white",
    font=("Arial", 12)
).pack()

operations = ["+", "-", "*", "/"]

operation_menu = tk.OptionMenu(
    root,
    operation_var,
    *operations
)
operation_menu.pack(pady=10)

# Button
calculate_btn = tk.Button(
    root,
    text="Calculate",
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12, "bold"),
    command=calculate
)
calculate_btn.pack(pady=15)

# Result
result_label = tk.Label(
    root,
    text="Result: ",
    bg="#1E3A5F",
    fg="yellow",
    font=("Arial", 14, "bold")
)
result_label.pack(pady=10)

root.mainloop()