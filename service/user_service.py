from model.repository.user_repository import UserRepository
from tools.validator import Validator

class UserService:
    def __init__(self):
        self.repo = UserRepository()
        self.validator = Validator()

    def add_user(self, user):
        if not self.validator.is_valid_email(user.email):
            raise ValueError("Invalid email")
        return self.repo.save(user)

    def update_user(self, user):
        if not self.validator.is_valid_email(user.email):
            raise ValueError("Invalid email")
        return self.repo.edit(user)

    def delete_user(self, user_id):
        return self.repo.delete(user_id)

    def get_all_users(self):
        return self.repo.find_all()

    def get_user_by_id(self, user_id):
        return self.repo.find_by_id(user_id)
