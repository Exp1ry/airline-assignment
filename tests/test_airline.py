import pytest
from models.airline import Airline

def test_airline_creation():
    """Test the creation of a new Airline instance.
    
    Verifies that:
    1. The ID is initially None
    2. The type is set to 'airline'
    3. The company name is an empty string
    """
    airline = Airline()
    assert airline.id is None
    assert airline.type == 'airline'
    assert airline.company_name == ""

def test_airline_to_dict():
    """Test the conversion of an Airline instance to a dictionary.
    
    Verifies that:
    1. The ID is correctly converted
    2. The type is preserved
    3. The company name is correctly stored
    """
    airline = Airline()
    airline.id = 1
    airline.company_name = "Test Airlines"
    
    data = airline.to_dict()
    assert data['id'] == 1
    assert data['type'] == 'airline'
    assert data['company_name'] == "Test Airlines"

def test_airline_from_dict():
    """Test the creation of an Airline instance from a dictionary.
    
    Verifies that:
    1. The ID is correctly loaded
    2. The type is preserved
    3. The company name is correctly loaded
    """
    data = {
        'id': 1,
        'type': 'airline',
        'company_name': "Test Airlines"
    }
    
    airline = Airline.from_dict(data)
    assert airline.id == 1
    assert airline.type == 'airline'
    assert airline.company_name == "Test Airlines" 