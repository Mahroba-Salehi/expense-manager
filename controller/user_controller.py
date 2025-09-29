from service.user_service import UserService

class UserController:
    def __init__(self):
        self.service = UserService()

    def add_user(self, user):
        return self.service.add_user(user)

    def update_user(self, user):
        return self.service.update_user(user)

    def delete_user(self, user_id):
        return self.service.delete_user(user_id)

    def get_all_users(self):
        return self.service.get_all_users()

    def get_user_by_id(self, user_id):
        return self.service.get_user_by_id(user_id)

    def get_user_by_email(self, email):
        return self.service.repo.find_by_email(email)
