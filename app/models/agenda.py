from app import db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy() 

class Block(db.Model):
    __tablename__ = 'blocks'
    id = db.Column(db.Integer, primary_key=True)
    professional_id = db.Column(db.Integer, db.ForeignKey("professionals.id") ,  nullable=False)
    unit_id = db.Column(db.Integer, db.ForeignKey("units.id"), nullable=False)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)
    ability = db.Column(db.Integer, default=1) # Capacidad (ej. 2 pacientes simultáneos)
    state = db.Column(db.String(20), default='open') # open, close, reserved

    professional = db.relationship("Professional", backref=db.backref("blocks", lazy=True))
    unit = db.relationship("Unit", backref=db.backref("blocks", lazy=True))