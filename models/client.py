from . import BaseModel

class Client(BaseModel):
    """Model class representing a client in the system.
    
    This class manages client information including personal details and address.
    
    Attributes:
        name (str): Full name of the client.
        address_line1 (str): Primary address line.
        address_line2 (str): Secondary address line (optional).
        address_line3 (str): Tertiary address line (optional).
        city (str): City of residence.
        state (str): State or province of residence.
        zip_code (str): Postal or ZIP code.
        country (str): Country of residence.
        phone_number (str): Contact phone number.
    """
    
    def __init__(self):
        """Initialize a new Client instance with default values."""
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
        """Convert the client instance to a dictionary.
        
        Returns:
            dict: Dictionary containing client data with all fields.
        """
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
        """Create a client instance from a dictionary.
        
        Args:
            data (dict): Dictionary containing client data.
            
        Returns:
            Client: New client instance with data from the dictionary.
        """
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