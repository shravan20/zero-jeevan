from app import db

class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    retreat_id = db.Column(db.Integer, db.ForeignKey('retreats.id'), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False)  
    payment_details = db.Column(db.String, nullable=False) 
    # Stores payment mode = [CREDIT_CARD, CASH, COUPON_CARD]
    # TODO: Add separate table/json for maintaining this information

    user = db.relationship('User', back_populates='bookings')
    retreat = db.relationship('Retreat', back_populates='bookings')

    def __repr__(self):
        return f'<Booking {self.user_id} at {self.retreat_id}>'
