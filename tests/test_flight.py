import pytest
from datetime import datetime
from models.flight import Flight

def test_flight_creation():
    flight = Flight()
    assert flight.id is None
    assert flight.type == 'flight'
    assert flight.client_id is None
    assert flight.airline_id is None
    assert isinstance(flight.date, datetime)
    assert flight.start_city == ""
    assert flight.end_city == ""

def test_flight_to_dict():
    flight = Flight()
    flight.id = 1
    flight.client_id = 100
    flight.airline_id = 200
    flight.start_city = "New York"
    flight.end_city = "Los Angeles"
    
    data = flight.to_dict()
    assert data['id'] == 1
    assert data['type'] == 'flight'
    assert data['client_id'] == 100
    assert data['airline_id'] == 200
    assert isinstance(data['date'], str)
    assert data['start_city'] == "New York"
    assert data['end_city'] == "Los Angeles"

def test_flight_from_dict():
    test_date = datetime.now().isoformat()
    data = {
        'id': 1,
        'type': 'flight',
        'client_id': 100,
        'airline_id': 200,
        'date': test_date,
        'start_city': "New York",
        'end_city': "Los Angeles"
    }
    
    flight = Flight.from_dict(data)
    assert flight.id == 1
    assert flight.type == 'flight'
    assert flight.client_id == 100
    assert flight.airline_id == 200
    assert isinstance(flight.date, datetime)
    assert flight.start_city == "New York"
    assert flight.end_city == "Los Angeles" 