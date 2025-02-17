from app import db
from app.models.user_model import User
from sqlalchemy.exc import IntegrityError

class UserRepository:
    def user_exists(self, email, phone):
        query = User.query
        if email:
            query = query.filter_by(email=email)
        if phone:
            query = query.filter_by(phone=phone)
        return query.first() is not None

    def add_user(self, data):
        user = User(
            name=data['name'],
            email=data['email'],
            phone=data['phone']
        ) # type: ignore

        try:
            db.session.add(user)
            db.session.commit()
            return {"message": "User created successfully", "data":user}, 201
        except IntegrityError:
            db.session.rollback()
            return {"message": "Error creating user"}, 500
    
    def get_users(self):
        try:
            users = User.query.all()
            return [user.to_dict() for user in users], 200
        except Exception as e:
            return {"message": str(e)}, 500
