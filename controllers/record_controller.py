from models.client import Client
from models.airline import Airline
from models.flight import Flight
import os

class RecordController:
    def __init__(self):
        self.data_dir = "data"
        self.records_file = os.path.join(self.data_dir, "records.json")
        self.records = []
        self._ensure_data_directory()
        self._load_records()
    
    def _ensure_data_directory(self):
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
    
    def _load_records(self):
        self.records = Client.load_records(self.records_file)
    
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
        for record in self.records:
            if record['id'] == record_id:
                record.update(data)
                self._save_records()
                return True
        return False
    
    def search_record(self, record_id):
        for record in self.records:
            if record['id'] == record_id:
                return record
        return None
    
    def get_all_records(self, record_type=None):
        if record_type:
            return [r for r in self.records if r['type'] == record_type]
        return self.records 