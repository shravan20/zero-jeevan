from app.repositories.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def create_user(self, data):
        if self.repository.user_exists(data['email'], data['phone']):
            return {"message": "User with this email already exists"}, 400

        return self.repository.add_user(data)
    
    def get_users(self):
        return self.repository.get_users()
    
    def user_exists(self, email, phone, need_data=False):
        user  = self.repository.user_exists(email, phone, need_data)
        if user:
            if need_data:
                return user
            return {"message": "User with this email already exists"}, 400
