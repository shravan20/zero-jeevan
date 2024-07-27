from app.services.retreat_service import RetreatService
from app.services.user_service import UserService
from app.repositories.booking_repository import BookingRepository

class BookingService:
    
    def __init__(self):
        self.repository = BookingRepository()
        self.retreat_service = RetreatService()
        self.user_service = UserService()

    def create_booking(self, data):
        user_id = data.get('user_id')
        user_name = data.get('user_name')
        user_email = data.get('user_email')
        user_phone = data.get('user_phone')
        retreat_id = data['retreat_id']
        booking_date = data['booking_date']
        payment_details = data['payment_details']

        if not self.retreat_service.get_retreat_by_id(retreat_id):
            return {"message": "Retreat does not exist"}, 400

        user = self.user_service.user_exists(email=user_email, phone=user_phone)
        if not user:
            new_user = {
                'name':user_name,
                'email':user_email,
                'phone':user_phone
                }
            user, status = self.user_service.create_user(new_user)
            if status != 201:
                return user, status
            user_id = user['id']

        existing_booking = self.repository.find_booking(user_id, retreat_id)
        if existing_booking:
            return {"message": "Booking already exists for this user and retreat"}, 400

        return self.repository.add_booking(user_id, retreat_id, booking_date, payment_details)
