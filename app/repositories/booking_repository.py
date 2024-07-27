from sqlalchemy.exc import IntegrityError
from app.models.booking_model import Booking
from app.models.user_model import User
from models.retreat_model import Retreat
from app import db

class BookingRepository:
    
    def add_booking(self, user_id, retreat_id, booking_date, payment_details):
        try:
            booking = Booking(
                user_id=user_id,
                retreat_id=retreat_id,
                booking_date=booking_date,
                payment_details=payment_details
            ) # type: ignore

            db.session.add(booking)
            db.session.commit()
            return {"message": "Booking created successfully"}, 201
        
        except IntegrityError:
            db.session.rollback()
            return {"message": "Error creating booking or duplicate booking"}, 500

    def find_booking(self, user_id, retreat_id):
        return db.session.query(Booking).filter_by(user_id=user_id, retreat_id=retreat_id).first()
