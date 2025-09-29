from model.repository.income_repository import IncomeRepository
from tools.validator import Validator

class IncomeService:
    def __init__(self):
        self.repo = IncomeRepository()
        self.validator = Validator()

    def add_income(self, income):
        if not self.validator.is_positive(income.amount):
            raise ValueError("Amount must be positive")
        if not self.validator.is_valid_date(income.date):
            raise ValueError("Invalid date format")
        return self.repo.save(income)

    def update_income(self, income):
        if not self.validator.is_positive(income.amount):
            raise ValueError("Amount must be positive")
        return self.repo.edit(income)

    def delete_income(self, income_id):
        return self.repo.delete(income_id)

    def get_all_incomes(self):
        return self.repo.find_all()

    def get_income_by_id(self, income_id):
        return self.repo.find_by_id(income_id)

    def get_income_by_date(self, date):
        return self.repo.find_by_date(date)
