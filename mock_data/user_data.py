from sqlalchemy import create_engine, Column, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = str(os.getenv('SQLALCHEMY_DATABASE_URI'))

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone
        }

Base.metadata.create_all(engine)

user_data = [
    {"name": "Alice", "email": "alice@example.com", "phone": "123-456-7890"},
    {"name": "Bob", "email": "bob@example.com", "phone": "234-567-8901"},
    {"name": "Charlie", "email": "charlie@example.com", "phone": "345-678-9012"},
]

for user in user_data:
    new_user = User(name=user['name'], email=user['email'], phone=user['phone'])
    session.add(new_user)

session.commit()

session.close()
