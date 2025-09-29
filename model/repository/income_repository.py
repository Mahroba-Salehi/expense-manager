from model.repository.database_manager import transaction_manager

class IncomeRepository:
    def save(self, income):
        return transaction_manager(
            "INSERT INTO incomes (user_id, amount, description, date) VALUES (?, ?, ?, ?)",
            [income.user_id, income.amount, income.description, income.date],
            commit=True
        )

    def edit(self, income):
        return transaction_manager(
            "UPDATE incomes SET user_id=?, amount=?, description=?, date=? WHERE id=?",
            [income.user_id, income.amount, income.description, income.date, income.id],
            commit=True
        )

    def delete(self, income_id):
        return transaction_manager(
            "DELETE FROM incomes WHERE id=?",
            [income_id],
            commit=True
        )

    def find_all(self):
        return transaction_manager("SELECT * FROM incomes")

    def find_by_id(self, income_id):
        return transaction_manager(
            "SELECT * FROM incomes WHERE id=?",
            [income_id]
        )

    def find_by_date(self, date):
        return transaction_manager(
            "SELECT * FROM incomes WHERE date=?",
            [date]
        )
