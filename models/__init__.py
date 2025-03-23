from abc import ABC, abstractmethod
from datetime import datetime
import json
import os

class BaseModel(ABC):
    def __init__(self):
        self.id = None
        self.type = self.__class__.__name__.lower()
    
    @abstractmethod
    def to_dict(self):
        pass
    
    @classmethod
    @abstractmethod
    def from_dict(cls, data):
        pass
    
    @staticmethod
    def save_records(records, filename):
        """Save records to a JSON file."""
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
        """Load records from a JSON file."""
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
    def __init__(self):
        super().__init__()
        self.airline_id = None
        self.client_id = None
        self.start_city = None
        self.end_city = None
        self.date = None
    
    def to_dict(self):
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
        flight = cls()
        flight.id = data.get('id')
        flight.airline_id = data.get('airline_id')
        flight.client_id = data.get('client_id')
        flight.start_city = data.get('start_city')
        flight.end_city = data.get('end_city')
        flight.date = data.get('date')
        return flight 