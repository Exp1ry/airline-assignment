import os
from models.client import Client
from models.airline import Airline
from models.flight import Flight


class RecordController:
    """Controller class for managing record operations.
    
    This class handles all record-related operations including creation, deletion,
    updating, and searching of records. It manages the persistence of records
    in a JSON file and provides methods for record manipulation.
    
    Attributes:
        data_dir (str): Directory path for storing data files.
        records_file (str): Path to the JSON file storing all records.
        records (list): List of all records in memory.
    """
    
    def __init__(self):
        """Initialize the record controller.
        
        Sets up the data directory and records file, then loads existing records
        from the JSON file.
        """
        self.data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
        self.records_file = os.path.join(self.data_dir, 'records.json')
        self.records = []
        self._ensure_data_directory()
        self._load_records()
    
    def _ensure_data_directory(self):
        """Ensure the data directory and records file exist.
        
        Creates the data directory and initializes an empty records file if they
        don't already exist.
        """
        if not os.path.exists(self.data_dir):
            print(f"Creating data directory: {self.data_dir}")
            os.makedirs(self.data_dir)
        
        if not os.path.exists(self.records_file):
            print(f"Creating records file: {self.records_file}")
            with open(self.records_file, 'w') as f:
                f.write('[]')  # Initialize with empty JSON array
    
    def _load_records(self):
        """Load records from the JSON file and convert them to appropriate model types.
        
        Reads the records file and converts each record to its appropriate model type
        (Client, Airline, or Flight) based on the record type field.
        
        Note:
            If there are any errors loading individual records, they are logged
            and skipped, allowing the loading process to continue.
        """
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
        """Save all records to the JSON file.
        
        Writes the current state of all records to the records file.
        """
        Client.save_records(self.records, self.records_file)
    
    def _get_next_id(self):
        """Get the next available record ID.
        
        Returns:
            int: The next available ID (highest existing ID + 1).
        """
        if not self.records:
            return 1
        return max(record['id'] for record in self.records) + 1
    
    def create_record(self, record_type, data):
        """Create a new record of the specified type.
        
        Args:
            record_type (str): Type of record to create ('client', 'airline', or 'flight').
            data (dict): Dictionary containing the record data.
            
        Returns:
            BaseModel: The newly created record instance.
            
        Raises:
            ValueError: If the record type is not recognized.
        """
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
        """Delete a record by ID.
        
        Args:
            record_id (int): The ID of the record to delete.
        """
        self.records = [r for r in self.records if r['id'] != record_id]
        self._save_records()
    
    def update_record(self, record_id, data):
        """Update a record by ID.
        
        Args:
            record_id (int): The ID of the record to update.
            data (dict): Dictionary containing the updated data.
            
        Returns:
            bool: True if record was updated, False if not found.
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
        """Search for a record by ID.
        
        Args:
            record_id (int): The ID of the record to search for.
            
        Returns:
            dict: The found record or None if not found.
            
        Note:
            Handles conversion of record_id to integer and provides error handling
            for invalid ID formats.
        """
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
        """Get all records.
        
        Returns:
            list: List of all records.
        """
        return self.records
    
    def get_all_records(self, record_type=None):
        """Get all records of a specific type.
        
        Args:
            record_type (str, optional): Type of records to retrieve.
                If None, returns all records.
                
        Returns:
            list: List of records of the specified type, or all records if no type
                is specified.
        """
        if record_type:
            return [r for r in self.records if r['type'] == record_type]
        return self.records
