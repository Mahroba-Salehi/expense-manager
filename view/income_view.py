import tkinter as tk
from tkinter import messagebox
from controller.income_controller import IncomeController
from model.entity.income import Income

class IncomeView:
    def __init__(self, master):
        self.controller = IncomeController()
        self.window = tk.Toplevel(master)
        self.window.title("Add Income")
        self.window.geometry("300x250")

        tk.Label(self.window, text="Amount").pack()
        self.amount_entry = tk.Entry(self.window)
        self.amount_entry.pack()

        tk.Label(self.window, text="Description").pack()
        self.desc_entry = tk.Entry(self.window)
        self.desc_entry.pack()

        tk.Label(self.window, text="Date (YYYY-MM-DD)").pack()
        self.date_entry = tk.Entry(self.window)
        self.date_entry.pack()

        tk.Button(self.window, text="Save", command=self.save_income).pack(pady=10)

    def save_income(self):
        try:
            amount = float(self.amount_entry.get())
            desc = self.desc_entry.get()
            date = self.date_entry.get()
            income = Income(None, 1, amount, desc, date)  # user_id = 1 (example)
            self.controller.add_income(income)
            messagebox.showinfo("Success", "Income added!")
            self.window.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

            self.reset_form()
            self.window.mainloop()
