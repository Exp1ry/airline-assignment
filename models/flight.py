from . import BaseModel
from datetime import datetime

class Flight(BaseModel):
    """Model class representing a flight in the system.
    
    This class manages flight information including client and airline associations,
    scheduling, and routing details.
    
    Attributes:
        client_id (int): ID of the client booking the flight.
        airline_id (int): ID of the airline operating the flight.
        date (datetime): Date and time of the flight.
        start_city (str): Departure city of the flight.
        end_city (str): Arrival city of the flight.
    """
    
    def __init__(self):
        """Initialize a new Flight instance with default values.
        
        Sets the date to the current time by default.
        """
        super().__init__()
        self.client_id = None
        self.airline_id = None
        self.date = datetime.now()
        self.start_city = ""
        self.end_city = ""
    
    def to_dict(self):
        """Convert the flight instance to a dictionary.
        
        Returns:
            dict: Dictionary containing flight data with all fields.
                The date is converted to ISO format string.
        """
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
        """Create a flight instance from a dictionary.
        
        Args:
            data (dict): Dictionary containing flight data.
                The date should be in ISO format string.
            
        Returns:
            Flight: New flight instance with data from the dictionary.
        """
        flight = cls()
        flight.id = data['id']
        flight.client_id = data['client_id']
        flight.airline_id = data['airline_id']
        flight.date = datetime.fromisoformat(data['date'])
        flight.start_city = data['start_city']
        flight.end_city = data['end_city']
        return flight 