from app import db

class Retreat(db.Model):
    __tablename__ = 'retreats'
    id = db.Column(db.Integer, primary_key=True, unique=True)
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

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'date': self.date.isoformat() if self.date else None,
            'location': self.location,
            'price': self.price,
            'type': self.type,
            'condition': self.condition,
            'image': self.image,
            'tag': self.tag,
            'duration': self.duration
        }
