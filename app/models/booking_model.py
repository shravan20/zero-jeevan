from app import db

class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    retreat_id = db.Column(db.Integer, db.ForeignKey('retreats.id'), nullable=False)

    user = db.relationship('User', back_populates='bookings')
    retreat = db.relationship('Retreat', back_populates='bookings')

    def __repr__(self):
        return f'<Booking {self.user_id} at {self.retreat_id}>'
