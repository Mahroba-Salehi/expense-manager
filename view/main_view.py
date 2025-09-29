from service.expense_service import ExpenseService
from model.entity.expense import Expense

def menu():
    service = ExpenseService()

    while True:
        print("\n1. Add Expense\n2. Show All\n3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            amount = float(input("Amount: "))
            category = input("Category: ")
            desc = input("Description: ")
            date = input("Date (YYYY-MM-DD): ")
            exp = Expense(None, 1, amount, category, desc, date)
            service.add_expense(exp)
            print("Expense saved!")
        elif choice == "2":
            print(service.repo.find_all())
        elif choice == "3":
            break
