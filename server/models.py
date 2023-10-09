from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db' 
db = SQLAlchemy(app)


class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.string(80), unique=True, nullable=False)
    event_description = db.Column(db.string(120), nullable=False)
    location = db.Column(db.string(120), unique=True, nullable=False)
    date_and_time = db.Column(db.string(120), nullable=False)
    ticket_quantity = db.Column(db.integer, default=0, nullable=False)
    ticket_type = db.Column(db.string(120), nullable=False)
    ticket_price = db.Column(db.integer, default=0, nullable=False)


    def __init__(self, event_name, event_description, location, date_and_time, ticket_quantity, ticket_type, ticket_price):
        self.event_name = event_name
        self.event_description = event_description
        self.location = location
        self.date_and_time = date_and_time
        self.ticket_quantity = ticket_quantity
        self.ticket_type = ticket_type
        self.ticket_price = ticket_price





                             
















    