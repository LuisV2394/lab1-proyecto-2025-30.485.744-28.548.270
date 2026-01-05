from app import db
from datetime import datetime

class Prescription(db.Model):
    __tablename__ = 'prescriptions'

    id = db.Column(db.Integer, primary_key=True)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    items = db.Column(db.JSON, nullable=False)
    observations = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    episode = db.relationship("Episode", backref="prescriptions")

    def to_dict(self):
        return {
            "id": self.id,
            "episode_id": self.episode_id,
            "items": self.items,
            "observations": self.observations,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }