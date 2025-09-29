from service.income_service import IncomeService

class IncomeController:
    def __init__(self):
        self.service = IncomeService()

    def add_income(self, income):
        return self.service.add_income(income)

    def update_income(self, income):
        return self.service.update_income(income)

    def delete_income(self, income_id):
        return self.service.delete_income(income_id)

    def get_all_incomes(self):
        return self.service.get_all_incomes()

    def get_income_by_id(self, income_id):
        return self.service.get_income_by_id(income_id)

    def get_income_by_date(self, date):
        return self.service.get_income_by_date(date)
