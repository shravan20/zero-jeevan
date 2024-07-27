from app import db
from app.models.retreat_model import Retreat
from sqlalchemy.exc import IntegrityError

class RetreatRepository:
    def filter_retreats(self, filters):
        query = Retreat.query

        for key, value in filters.items():
            if hasattr(Retreat, key):
                if isinstance(value, list):
                    query = query.filter(getattr(Retreat, key).in_(value))
                else:
                    query = query.filter(getattr(Retreat, key) == value)
        
        return query

    def get_retreats(self, filters=None, page=1, limit=10):
        query = self.filter_retreats(filters) if filters else Retreat.query

        total = query.count()
        retreats = query.offset((page - 1) * limit).limit(limit).all()

        return retreats, total

    def get_retreat_by_id(self, retreat_id):
        return Retreat.query.get(retreat_id)
    
    def add_retreat(self, data):
        retreat = Retreat(
            title=data['title'],
            description=data['description'],
            date=data['date'],
            location=data['location'],
            price=data['price'],
            type=data['type'],
            condition=data['condition'],
            image=data.get('image'),
            tag=data.get('tag', []),
            duration=data['duration']
        ) # type: ignore

        try:
            db.session.add(retreat)
            db.session.commit()
            return retreat.to_dict(), 201
        except IntegrityError:
            db.session.rollback()
            return {"message": "Error creating retreat"}, 500

    def find_by_title_and_date(self, title, date):
        return db.session.query(Retreat).filter_by(title=title, date=date).first()
