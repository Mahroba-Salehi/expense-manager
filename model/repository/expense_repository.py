from model.repository.database_manager import transaction_manager

class ExpenseRepository:
    def save(self, expense):
        return transaction_manager(
            "INSERT INTO expenses (user_id, amount, category, description, date) VALUES (?, ?, ?, ?, ?)",
            [expense.user_id, expense.amount, expense.category, expense.description, expense.date],
            commit=True
        )

    def edit(self, expense):
        return transaction_manager(
            "UPDATE expenses SET user_id=?, amount=?, category=?, description=?, date=? WHERE id=?",
            [expense.user_id, expense.amount, expense.category, expense.description, expense.date, expense.id],
            commit=True
        )

    def delete(self, expense_id):
        return transaction_manager(
            "DELETE FROM expenses WHERE id=?",
            [expense_id],
            commit=True
        )

    def find_all(self):
        return transaction_manager("SELECT * FROM expenses")

    def find_by_id(self, expense_id):
        return transaction_manager(
            "SELECT * FROM expenses WHERE id=?",
            [expense_id]
        )

    def find_by_category(self, category):
        return transaction_manager(
            "SELECT * FROM expenses WHERE category=?",
            [category]
        )

    def find_by_date(self, date):
        return transaction_manager(
            "SELECT * FROM expenses WHERE date=?",
            [date]
        )
