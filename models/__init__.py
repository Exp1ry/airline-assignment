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
        # Ensure all IDs are integers before saving
        for record in records:
            if 'id' in record:
                record['id'] = int(record['id'])
            if 'client_id' in record:
                record['client_id'] = int(record['client_id'])
            if 'airline_id' in record:
                record['airline_id'] = int(record['airline_id'])
        with open(filename, 'w') as f:
            json.dump(records, f, default=str)
    
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