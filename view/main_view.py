import tkinter as tk
from view.income_view import IncomeView
from view.expense_view import ExpenseView
from view.report_view import ReportView

class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Manager")
        self.root.geometry("400x300")

        tk.Label(root, text="Expense Manager", font=("Helvetica", 16)).pack(pady=20)

        tk.Button(root, text="Add Income", width=20, command=self.open_income).pack(pady=5)
        tk.Button(root, text="Add Expense", width=20, command=self.open_expense).pack(pady=5)
        tk.Button(root, text="Show Report", width=20, command=self.open_report).pack(pady=5)
        tk.Button(root, text="Exit", width=20, command=root.quit).pack(pady=5)

    def open_income(self):
        IncomeView(self.root)

    def open_expense(self):
        ExpenseView(self.root)

    def open_report(self):
        ReportView(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainView(root)
    root.mainloop()
