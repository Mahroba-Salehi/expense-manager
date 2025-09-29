import tkinter as tk
from controller.income_controller import IncomeController
from controller.expense_controller import ExpenseController
from tools.utils import Utils

class ReportView:
    def __init__(self, master):
        self.income_ctrl = IncomeController()
        self.expense_ctrl = ExpenseController()
        self.utils = Utils()

        self.window = tk.Toplevel(master)
        self.window.title("Financial Report")
        self.window.geometry("400x400")

        self.display_report()

    def display_report(self):
        incomes = self.income_ctrl.get_all_incomes()
        expenses = self.expense_ctrl.get_all_expenses()

        total_income = self.utils.calculate_total([type('R', (), {'amount': inc[2]})() for inc in incomes])
        total_expense = self.utils.calculate_total([type('R', (), {'amount': exp[2]})() for exp in expenses])

        tk.Label(self.window, text=f"Total Income: {self.utils.format_currency(total_income)}").pack()
        tk.Label(self.window, text=f"Total Expense: {self.utils.format_currency(total_expense)}").pack()

        tk.Label(self.window, text="--- Income Details ---").pack()
        for inc in incomes:
            tk.Label(self.window, text=f"{inc[3]} | {inc[2]}").pack()

        tk.Label(self.window, text="--- Expense Details ---").pack()
        for exp in expenses:
            tk.Label(self.window, text=f"{exp[3]} | {exp[2]} | {exp[4]}").pack()
