import pytest
import requests
from server.app import app



@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_get_events(client):
    response = client.get('/events')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 2  # Check the number of sample events

def test_get_event(client):
    response = client.get('/events/Music Festival')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, dict)
    assert data['name'] == 'Music Festival'

def test_get_nonexistent_event(client):
    response = client.get('/events/Nonexistent Event')
    assert response.status_code == 404
    data = response.get_json()
    assert 'message' in data
    assert data['message'] == 'Event not found'


# Define the event data as a dictionary
event_data = {
    "name": "Sample Event",
    "date": "2023-10-15",
    "time": "18:00",
    "location": "Sample Location",
    "tickets_available": 100,
    "ticket_price": 20.0
}

# Send a POST request to add the event
response = requests.post('http://localhost:5000/events', json=event_data)

# Check the response
if response.status_code == 201:
    print("Event added successfully")
else:
    print("Failed to add event:", response.json())
