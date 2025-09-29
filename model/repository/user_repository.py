from model.repository.database_manager import transaction_manager

class UserRepository:
    def save(self, user):
        return transaction_manager(
            "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
            [user.name, user.email, user.password],
            commit=True
        )

    def edit(self, user):
        return transaction_manager(
            "UPDATE users SET name=?, email=?, password=? WHERE id=?",
            [user.name, user.email, user.password, user.id],
            commit=True
        )

    def delete(self, user_id):
        return transaction_manager(
            "DELETE FROM users WHERE id=?",
            [user_id],
            commit=True
        )

    def find_all(self):
        return transaction_manager("SELECT * FROM users")

    def find_by_id(self, user_id):
        return transaction_manager(
            "SELECT * FROM users WHERE id=?",
            [user_id]
        )

    def find_by_email(self, email):
        return transaction_manager(
            "SELECT * FROM users WHERE email=?",
            [email]
        )
