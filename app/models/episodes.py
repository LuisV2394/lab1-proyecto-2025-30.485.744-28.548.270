# Episodes
from app import db
from datetime import datetime

class Episode(db.Model):
    __tablename__ = 'episodes'
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("people.id"), nullable=False)
    opening_date = db.Column(db.DateTime, default=datetime.utcnow)
    reason = db.Column(db.String(255))
    # kind: consultation, process, check, outpatient_emergency
    kind = db.Column(db.String(50), nullable=False) 
    status = db.Column(db.String(10), default='open') # open, close

# Relationships
    person = db.relationship("Person", backref=db.backref("episodes", lazy=True))   