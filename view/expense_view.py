import tkinter as tk
from tkinter import messagebox
from controller.expense_controller import ExpenseController
from model.entity.expense import Expense

class ExpenseView:
    def __init__(self, master):
        self.controller = ExpenseController()
        self.window = tk.Toplevel(master)
        self.window.title("Add Expense")
        self.window.geometry("300x300")

        tk.Label(self.window, text="Amount").pack()
        self.amount_entry = tk.Entry(self.window)
        self.amount_entry.pack()

        tk.Label(self.window, text="Category").pack()
        self.category_entry = tk.Entry(self.window)
        self.category_entry.pack()

        tk.Label(self.window, text="Description").pack()
        self.desc_entry = tk.Entry(self.window)
        self.desc_entry.pack()

        tk.Label(self.window, text="Date (YYYY-MM-DD)").pack()
        self.date_entry = tk.Entry(self.window)
        self.date_entry.pack()

        tk.Button(self.window, text="Save", command=self.save_expense).pack(pady=10)

    def save_expense(self):
        try:
            amount = float(self.amount_entry.get())
            category = self.category_entry.get()
            desc = self.desc_entry.get()
            date = self.date_entry.get()
            expense = Expense(None, 1, amount, category, desc, date)  # user_id = 1
            self.controller.add_expense(expense)
            messagebox.showinfo("Success", "Expense added!")
            self.window.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
