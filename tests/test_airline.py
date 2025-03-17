import pytest
from models.airline import Airline

def test_airline_creation():
    airline = Airline()
    assert airline.id is None
    assert airline.type == 'airline'
    assert airline.company_name == ""

def test_airline_to_dict():
    airline = Airline()
    airline.id = 1
    airline.company_name = "Test Airlines"
    
    data = airline.to_dict()
    assert data['id'] == 1
    assert data['type'] == 'airline'
    assert data['company_name'] == "Test Airlines"

def test_airline_from_dict():
    data = {
        'id': 1,
        'type': 'airline',
        'company_name': "Test Airlines"
    }
    
    airline = Airline.from_dict(data)
    assert airline.id == 1
    assert airline.type == 'airline'
    assert airline.company_name == "Test Airlines" 