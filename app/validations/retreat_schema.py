from marshmallow import Schema, fields, validate, ValidationError # type: ignore
from datetime import datetime
import re

def validate_url(value):
    url_pattern = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
        r'localhost|' # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if not re.match(url_pattern, value):
        raise ValidationError("Invalid URL")
    

class RetreatSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(min=1))
    description = fields.String(required=True, validate=validate.Length(min=1))
    date = fields.Date(required=True)
    location = fields.String(required=True, validate=validate.Length(min=1))
    price = fields.Float(required=True, validate=validate.Range(min=0))
    type = fields.String(required=True, validate=validate.Length(min=1))
    condition = fields.String(required=True, validate=validate.Length(min=1))
    image = fields.String(validate=validate_url)
    tag = fields.List(fields.String(), validate=validate.Length(min=1))
    duration = fields.Integer(required=True, validate=validate.Range(min=1))
