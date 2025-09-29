from service.expense_service import ExpenseService

class ExpenseController:
    def __init__(self):
        self.service = ExpenseService()

    def add_expense(self, expense):
        return self.service.add_expense(expense)

    def update_expense(self, expense):
        return self.service.update_expense(expense)

    def delete_expense(self, expense_id):
        return self.service.delete_expense(expense_id)

    def get_all_expenses(self):
        return self.service.get_all_expenses()

    def get_expense_by_id(self, expense_id):
        return self.service.get_expense_by_id(expense_id)

    def get_expense_by_category(self, category):
        return self.service.get_expense_by_category(category)

    def get_expense_by_date(self, date):
        return self.service.get_expense_by_date(date)
