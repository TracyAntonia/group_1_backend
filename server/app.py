from flask import Flask, jsonify

app = Flask(__name__)

# Sample event data
events = [
    {
        "name": "Music Festival",
        "date": "2023-10-15",
        "time": "18:00",
        "location": "City Park",
        "tickets_available": 500,
        "ticket_price": 25.00,
    },
    {
        "name": "Food Fair",
        "date": "2023-11-05",
        "time": "12:00",
        "location": "Downtown Square",
        "tickets_available": 200,
        "ticket_price": 10.00,
    },
    # Add more events here
]

# Route to get a list of all events
@app.route('/events', methods=['GET'])
def get_events():
    return jsonify(events)

# Route to get details of a specific event by name
@app.route('/events/<event_name>', methods=['GET'])
def get_event(event_name):
    event = next((event for event in events if event['name'] == event_name), None)
    if event:
        return jsonify(event)
    else:
        return jsonify({"message": "Event not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
