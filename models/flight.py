from . import BaseModel
from datetime import datetime

class Flight(BaseModel):
    def __init__(self):
        super().__init__()
        self.client_id = None
        self.airline_id = None
        self.date = datetime.now()
        self.start_city = ""
        self.end_city = ""
    
    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'client_id': self.client_id,
            'airline_id': self.airline_id,
            'date': self.date.isoformat(),
            'start_city': self.start_city,
            'end_city': self.end_city
        }
    
    @classmethod
    def from_dict(cls, data):
        flight = cls()
        flight.id = data['id']
        flight.client_id = data['client_id']
        flight.airline_id = data['airline_id']
        flight.date = datetime.fromisoformat(data['date'])
        flight.start_city = data['start_city']
        flight.end_city = data['end_city']
        return flight 