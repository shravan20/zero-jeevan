from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    phone = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

    def to_dict(self):
            return {
                'id': self.id,
                'name': self.name,
                'email': self.email,
                'phone': self.phone
            }
