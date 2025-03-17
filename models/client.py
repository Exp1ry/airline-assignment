from . import BaseModel

class Client(BaseModel):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.address_line1 = ""
        self.address_line2 = ""
        self.address_line3 = ""
        self.city = ""
        self.state = ""
        self.zip_code = ""
        self.country = ""
        self.phone_number = ""
    
    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'name': self.name,
            'address_line1': self.address_line1,
            'address_line2': self.address_line2,
            'address_line3': self.address_line3,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code,
            'country': self.country,
            'phone_number': self.phone_number
        }
    
    @classmethod
    def from_dict(cls, data):
        client = cls()
        client.id = data['id']
        client.name = data['name']
        client.address_line1 = data['address_line1']
        client.address_line2 = data['address_line2']
        client.address_line3 = data['address_line3']
        client.city = data['city']
        client.state = data['state']
        client.zip_code = data['zip_code']
        client.country = data['country']
        client.phone_number = data['phone_number']
        return client 