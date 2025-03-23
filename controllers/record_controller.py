from models.client import Client
from models.airline import Airline
from models.flight import Flight
import os

class RecordController:
    def __init__(self):
        """Initialize the record controller."""
        self.data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
        self.records_file = os.path.join(self.data_dir, 'records.json')
        self.records = []
        self._ensure_data_directory()
        self._load_records()
    
    def _ensure_data_directory(self):
        """Ensure the data directory and records file exist."""
        if not os.path.exists(self.data_dir):
            print(f"Creating data directory: {self.data_dir}")
            os.makedirs(self.data_dir)
        
        if not os.path.exists(self.records_file):
            print(f"Creating records file: {self.records_file}")
            with open(self.records_file, 'w') as f:
                f.write('[]')  # Initialize with empty JSON array
    
    def _load_records(self):
        """Load records from the JSON file and convert them to appropriate model types."""
        try:
            print(f"Loading records from {self.records_file}")
            if not os.path.exists(self.records_file):
                print(f"Records file does not exist: {self.records_file}")
                self.records = []
                return
            
            if not os.access(self.records_file, os.R_OK):
                print(f"Records file is not readable: {self.records_file}")
                self.records = []
                return

            raw_records = Client.load_records(self.records_file)
            print(f"Raw records loaded: {raw_records}")
            self.records = []
            
            for record in raw_records:
                record_type = record.get('type', '').lower()
                print(f"Processing record: {record}")
                try:
                    if record_type == 'client':
                        self.records.append(Client.from_dict(record).to_dict())
                    elif record_type == 'airline':
                        self.records.append(Airline.from_dict(record).to_dict())
                    elif record_type == 'flight':
                        self.records.append(Flight.from_dict(record).to_dict())
                except Exception as e:
                    print(f"Error loading record: {e}")
                    continue
            print(f"Final loaded records: {self.records}")
        except Exception as e:
            print(f"Error loading records file: {e}")
            self.records = []
    
    def _save_records(self):
        Client.save_records(self.records, self.records_file)
    
    def _get_next_id(self):
        if not self.records:
            return 1
        return max(record['id'] for record in self.records) + 1
    
    def create_record(self, record_type, data):
        if record_type == 'client':
            record = Client()
            record.id = self._get_next_id()
            for key, value in data.items():
                setattr(record, key, value)
        elif record_type == 'airline':
            record = Airline()
            record.id = self._get_next_id()
            for key, value in data.items():
                setattr(record, key, value)
        elif record_type == 'flight':
            record = Flight()
            record.id = self._get_next_id()
            for key, value in data.items():
                setattr(record, key, value)
        else:
            raise ValueError(f"Unknown record type: {record_type}")
        
        self.records.append(record.to_dict())
        self._save_records()
        return record
    
    def delete_record(self, record_id):
        self.records = [r for r in self.records if r['id'] != record_id]
        self._save_records()
    
    def update_record(self, record_id, data):
        """Update a record by ID.
        
        Args:
            record_id: The ID of the record to update
            data: Dictionary containing the updated data
            
        Returns:
            bool: True if record was updated, False if not found
        """
        for record in self.records:
            if record['id'] == record_id:
                # Preserve the record type when updating
                data['type'] = record['type']
                record.update(data)
                self._save_records()
                return True
        return False
    
    def search_record(self, record_id):
        """Search for a record by ID."""
        try:
            record_id = int(record_id)  # Convert to int for comparison
            print(f"Searching for record with ID: {record_id}")
            print(f"Current records: {self.records}")
            
            for record in self.records:
                print(f"Checking record: {record}")
                current_id = int(record.get('id', -1))  # Convert record ID to int
                print(f"Comparing IDs: {current_id} == {record_id}")
                if current_id == record_id:
                    print(f"Found record: {record}")
                    return record
            print(f"No record found with ID: {record_id}")
            return None
        except ValueError as e:
            print(f"Invalid ID format: {e}")
            return None
        except Exception as e:
            print(f"Error during search: {e}")
            return None
    
    def get_records(self):
        """Get all records."""
        return self.records
    
    def get_all_records(self, record_type=None):
        if record_type:
            return [r for r in self.records if r['type'] == record_type]
        return self.records 