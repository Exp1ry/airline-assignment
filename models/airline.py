from . import BaseModel

class Airline(BaseModel):
    def __init__(self):
        super().__init__()
        self.company_name = ""
    
    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'company_name': self.company_name
        }
    
    @classmethod
    def from_dict(cls, data):
        airline = cls()
        airline.id = data['id']
        airline.company_name = data['company_name']
        return airline 