from app import db
from datetime import datetime

class ClinicalVersion(db.Model):
    __tablename__ = 'clinical_versions'

    id = db.Column(db.Integer, primary_key=True)
    
    # We identify what type of entity we are versioning('note' o 'result')
    entity_type = db.Column(db.String(100), nullable=False) 
    entity_id = db.Column(db.Integer, nullable=False)
    
    version_number = db.Column(db.Integer, nullable=False)
    content_snapshot = db.Column(db.JSON, nullable=False) # We save the entire previous content
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "entity_type": self.entity_type,
            "entity_id": self.entity_id,
            "version_number": self.version_number,
            "content_snapshot": self.content_snapshot,
            "user_id": self.user_id,
            "date": self.created_at.isoformat()
        }