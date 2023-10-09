from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.String(8), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    tickets_available = db.Column(db.Integer, nullable=False)
    ticket_price = db.Column(db.Float, nullable=False)

    def __init__(self, name, date, time, location, tickets_available, ticket_price):
        self.name = name
        self.date = date
        self.time = time
        self.location = location
        self.tickets_available = tickets_available
        self.ticket_price = ticket_price

# Route to get a list of all events
@app.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    event_list = []
    for event in events:
        event_data = {
            "name": event.name,
            "date": event.date.strftime('%Y-%m-%d'),
            "time": event.time,
            "location": event.location,
            "tickets_available": event.tickets_available,
            "ticket_price": event.ticket_price,
        }
        event_list.append(event_data)
    return jsonify(event_list)

# Route to get details of a specific event by name
@app.route('/events/<event_name>', methods=['GET'])
def get_event(event_name):
    event = Event.query.filter_by(name=event_name).first()
    if event:
        event_data = {
            "name": event.name,
            "date": event.date.strftime('%Y-%m-%d'),
            "time": event.time,
            "location": event.location,
            "tickets_available": event.tickets_available,
            "ticket_price": event.ticket_price,
        }
        return jsonify(event_data)
    else:
        return jsonify({"message": "Event not found"}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
