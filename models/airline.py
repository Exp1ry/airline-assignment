from . import BaseModel

class Airline(BaseModel):
    """Model class representing an airline company.
    
    This class manages airline information including company name and identification.
    
    Attributes:
        company_name (str): Name of the airline company.
    """
    
    def __init__(self):
        """Initialize a new Airline instance with default values."""
        super().__init__()
        self.company_name = ""
    
    def to_dict(self):
        """Convert the airline instance to a dictionary.
        
        Returns:
            dict: Dictionary containing airline data with all fields.
        """
        return {
            'id': self.id,
            'type': self.type,
            'company_name': self.company_name
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create an airline instance from a dictionary.
        
        Args:
            data (dict): Dictionary containing airline data.
            
        Returns:
            Airline: New airline instance with data from the dictionary.
        """
        airline = cls()
        airline.id = data['id']
        airline.company_name = data['company_name']
        return airline 