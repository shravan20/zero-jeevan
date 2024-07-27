from marshmallow import Schema, fields, validate, ValidationError

class BookingSchema(Schema):
    user_id = fields.Integer()
    user_name = fields.String(required=True)
    user_email = fields.Email(required=True)
    user_phone = fields.String(required=True)
    retreat_id = fields.Integer(required=True)
    retreat_title = fields.String(required=True)
    retreat_location = fields.String(required=True)
    retreat_price = fields.Float(required=True)
    retreat_duration = fields.Integer(required=True)
    booking_date = fields.Date(required=True)
    payment_details = fields.String(required=True, validate=validate.Length(min=1))
