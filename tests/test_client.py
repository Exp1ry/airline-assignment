import pytest
from models.client import Client

def test_client_creation():
    """Test the creation of a new Client instance.
    
    Verifies that:
    1. The ID is initially None
    2. The type is set to 'client'
    3. All address fields are empty strings
    4. All contact information fields are empty strings
    """
    client = Client()
    assert client.id is None
    assert client.type == 'client'
    assert client.name == ""
    assert client.address_line1 == ""
    assert client.address_line2 == ""
    assert client.address_line3 == ""
    assert client.city == ""
    assert client.state == ""
    assert client.zip_code == ""
    assert client.country == ""
    assert client.phone_number == ""

def test_client_to_dict():
    """Test the conversion of a Client instance to a dictionary.
    
    Verifies that:
    1. The ID is correctly converted
    2. The type is preserved
    3. All address fields are correctly stored
    4. All contact information fields are correctly stored
    """
    client = Client()
    client.id = 1
    client.name = "John Doe"
    client.address_line1 = "123 Main St"
    client.city = "New York"
    client.state = "NY"
    client.zip_code = "10001"
    client.country = "USA"
    client.phone_number = "555-0123"
    
    data = client.to_dict()
    assert data['id'] == 1
    assert data['type'] == 'client'
    assert data['name'] == "John Doe"
    assert data['address_line1'] == "123 Main St"
    assert data['city'] == "New York"
    assert data['state'] == "NY"
    assert data['zip_code'] == "10001"
    assert data['country'] == "USA"
    assert data['phone_number'] == "555-0123"

def test_client_from_dict():
    """Test the creation of a Client instance from a dictionary.
    
    Verifies that:
    1. The ID is correctly loaded
    2. The type is preserved
    3. All address fields are correctly loaded
    4. All contact information fields are correctly loaded
    5. Optional address fields (line2, line3) are handled properly
    """
    data = {
        'id': 1,
        'type': 'client',
        'name': "John Doe",
        'address_line1': "123 Main St",
        'address_line2': "",
        'address_line3': "",
        'city': "New York",
        'state': "NY",
        'zip_code': "10001",
        'country': "USA",
        'phone_number': "555-0123"
    }
    
    client = Client.from_dict(data)
    assert client.id == 1
    assert client.type == 'client'
    assert client.name == "John Doe"
    assert client.address_line1 == "123 Main St"
    assert client.city == "New York"
    assert client.state == "NY"
    assert client.zip_code == "10001"
    assert client.country == "USA"
    assert client.phone_number == "555-0123" 