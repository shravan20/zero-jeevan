from app.repositories.retreat_repository import RetreatRepository

class RetreatService:
    def __init__(self):
        self.repository = RetreatRepository()

    def get_retreats(self, filters=None, page=1, limit=10):
        retreats, total = self.repository.get_retreats(filters, page, limit)
        return {
            'retreats': [retreat.to_dict() for retreat in retreats],
            'total': total
        }, 200

    def get_retreat_by_id(self, retreat_id):
        retreat = self.repository.get_retreat_by_id(retreat_id)
        if retreat:
            return retreat.to_dict(), 200
        return {"message": "Retreat not found"}, 404
    
    
    def create_retreat(self, data):
            existing_retreat = self.repository.find_by_title_and_date(data['title'], data['date'])
            if existing_retreat:
                return {"message": "Retreat with the same title and date already exists"}, 400
            return self.repository.add_retreat(data)
