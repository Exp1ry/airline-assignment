# Travel Agent Record Management System

A Python-based record management system for a specialist travel agent, following the MVC (Model-View-Controller) pattern.

## Features

- Manage three types of records:
  - Client records
  - Flight records
  - Airline Company records
- Create, read, update, and delete records
- Graphical User Interface for easy interaction
- Persistent storage using JSON format
- Unit tests for all models

## Project Structure

```
airline/
├── models/           # Data models
├── views/           # GUI implementation
├── controllers/     # Business logic
├── data/           # Data storage
├── tests/          # Unit tests
└── main.py         # Application entry point
```

## Requirements

- Python 3.x
- tkinter (usually comes with Python)
- pytest (for running tests)
- python-dateutil

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

```bash
python main.py
```

## Running Tests

```bash
pytest tests/
```

## Record Formats

### Client Record

- ID: int
- Type: str
- Name: str
- Address Line 1: str
- Address Line 2: str
- Address Line 3: str
- City: str
- State: str
- Zip Code: str
- Country: str
- Phone Number: str

### Airline Record

- ID: int
- Type: str
- Company Name: str

### Flight Record

- ID: int
- Type: str
- Client_ID: int
- Airline_ID: int
- Date: datetime
- Start City: str
- End City: str
