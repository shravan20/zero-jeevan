from app import db

class Retreat(db.Model):
    __tablename__ = 'retreats'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=True)
    date = db.Column(db.DateTime, nullable=False)  
    location = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    type = db.Column(db.String, nullable=True)  
    condition = db.Column(db.String, nullable=True)  
    image = db.Column(db.String, nullable=True)  
    tag = db.Column(db.ARRAY(db.String), nullable=True)  
    duration = db.Column(db.Integer, nullable=False)  

    def __repr__(self):
        return f'<Retreat {self.title}>'
