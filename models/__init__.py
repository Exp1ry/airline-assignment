from abc import ABC, abstractmethod
from datetime import datetime
import json
import os

class BaseModel(ABC):
    """Base class for all data models in the application.
    
    This abstract base class provides common functionality for all model classes,
    including ID management, type identification, and record persistence.
    
    Attributes:
        id (int): Unique identifier for the record.
        type (str): Type of the model (derived from class name).
    """
    
    def __init__(self):
        """Initialize a new BaseModel instance."""
        self.id = None
        self.type = self.__class__.__name__.lower()
    
    @abstractmethod
    def to_dict(self):
        """Convert the model instance to a dictionary.
        
        Returns:
            dict: Dictionary representation of the model.
        """
        pass
    
    @classmethod
    @abstractmethod
    def from_dict(cls, data):
        """Create a model instance from a dictionary.
        
        Args:
            data (dict): Dictionary containing model data.
            
        Returns:
            BaseModel: New instance of the model class.
        """
        pass
    
    @staticmethod
    def save_records(records, filename):
        """Save records to a JSON file.
        
        Args:
            records (list): List of record dictionaries to save.
            filename (str): Path to the JSON file.
            
        Note:
            Automatically converts IDs to integers and formats dates.
        """
        # Ensure all IDs are integers before saving
        for record in records:
            if 'id' in record:
                record['id'] = int(record['id'])
            if 'client_id' in record:
                record['client_id'] = int(record['client_id'])
            if 'airline_id' in record:
                record['airline_id'] = int(record['airline_id'])
            # Handle date fields
            if 'date' in record:
                if isinstance(record['date'], datetime):
                    record['date'] = record['date'].strftime("%Y-%m-%d %H:%M:%S")
            if 'departure_date' in record:
                if isinstance(record['departure_date'], datetime):
                    record['departure_date'] = record['departure_date'].strftime("%Y-%m-%d %H:%M:%S")
            if 'arrival_date' in record:
                if isinstance(record['arrival_date'], datetime):
                    record['arrival_date'] = record['arrival_date'].strftime("%Y-%m-%d %H:%M:%S")
        with open(filename, 'w') as f:
            json.dump(records, f)
    
    @staticmethod
    def load_records(filename):
        """Load records from a JSON file.
        
        Args:
            filename (str): Path to the JSON file.
            
        Returns:
            list: List of record dictionaries.
            
        Note:
            Handles various encodings and converts string IDs to integers.
            Returns empty list if file doesn't exist or is invalid.
        """
        print(f"BaseModel.load_records called with filename: {filename}")
        if not os.path.exists(filename):
            print(f"File does not exist: {filename}")
            return []
        try:
            # Try different encodings
            encodings = ['utf-8', 'utf-8-sig', 'ascii']
            content = None
            
            for encoding in encodings:
                try:
                    with open(filename, 'r', encoding=encoding) as f:
                        content = f.read().strip()
                        print(f"Successfully read file with {encoding} encoding")
                        break
                except UnicodeDecodeError:
                    continue
            
            if content is None:
                print("Failed to read file with any encoding")
                return []
                
            print(f"File content: {content}")
            if not content:  # File is empty
                print("File is empty")
                return []
                
            # Try to parse the JSON
            try:
                records = json.loads(content)
                print(f"Loaded records: {records}")
                # Convert any string IDs back to integers
                for record in records:
                    if 'id' in record:
                        record['id'] = int(record['id'])
                    if 'client_id' in record:
                        record['client_id'] = int(record['client_id'])
                    if 'airline_id' in record:
                        record['airline_id'] = int(record['airline_id'])
                return records
            except json.JSONDecodeError as e:
                print(f"JSON decode error: {e}")
                # Try to fix common JSON issues
                content = content.replace('\n', '').replace('\r', '')
                try:
                    records = json.loads(content)
                    print(f"Successfully loaded records after cleaning")
                    return records
                except json.JSONDecodeError as e:
                    print(f"Still failed to decode JSON after cleaning: {e}")
                    return []
        except Exception as e:
            print(f"Unexpected error in load_records: {e}")
            return []

class Flight(BaseModel):
    """Model class representing a flight record.
    
    Attributes:
        airline_id (int): ID of the airline operating the flight.
        client_id (int): ID of the client booking the flight.
        start_city (str): Departure city of the flight.
        end_city (str): Arrival city of the flight.
        date (str): Date and time of the flight.
    """
    
    def __init__(self):
        """Initialize a new Flight instance."""
        super().__init__()
        self.airline_id = None
        self.client_id = None
        self.start_city = None
        self.end_city = None
        self.date = None
    
    def to_dict(self):
        """Convert the flight instance to a dictionary.
        
        Returns:
            dict: Dictionary containing flight data with all fields.
        """
        return {
            'id': self.id,
            'type': self.type,
            'airline_id': self.airline_id,
            'client_id': self.client_id,
            'start_city': self.start_city,
            'end_city': self.end_city,
            'date': str(self.date) if self.date else None
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create a flight instance from a dictionary.
        
        Args:
            data (dict): Dictionary containing flight data.
            
        Returns:
            Flight: New flight instance with data from the dictionary.
        """
        flight = cls()
        flight.id = data.get('id')
        flight.airline_id = data.get('airline_id')
        flight.client_id = data.get('client_id')
        flight.start_city = data.get('start_city')
        flight.end_city = data.get('end_city')
        flight.date = data.get('date')
        return flight 