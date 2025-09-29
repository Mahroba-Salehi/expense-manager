from model.repository.expense_repository import ExpenseRepository
from tools.validator import Validator

class ExpenseService:
    def __init__(self):
        self.repo = ExpenseRepository()
        self.validator = Validator()

    def add_expense(self, expense):
        if not self.validator.is_positive(expense.amount):
            raise ValueError("Amount must be positive")
        if not self.validator.is_not_empty(expense.category):
            raise ValueError("Category cannot be empty")
        if not self.validator.is_valid_date(expense.date):
            raise ValueError("Invalid date format")
        return self.repo.save(expense)

    def update_expense(self, expense):
        if not self.validator.is_positive(expense.amount):
            raise ValueError("Amount must be positive")
        return self.repo.edit(expense)

    def delete_expense(self, expense_id):
        return self.repo.delete(expense_id)

    def get_all_expenses(self):
        return self.repo.find_all()

    def get_expense_by_id(self, expense_id):
        return self.repo.find_by_id(expense_id)

    def get_expense_by_category(self, category):
        return self.repo.find_by_category(category)

    def get_expense_by_date(self, date):
        return self.repo.find_by_date(date)
