from app import db
from datetime import datetime

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    
    # type: laboratory, imaging, procedure
    type = db.Column(db.String(50), nullable=False)
    
    # details: array of objects {code, description, instructions}
    # En MySQL esto se guarda como JSON nativo
    details = db.Column(db.JSON, nullable=False)
    
    # priority: normal/urgent
    priority = db.Column(db.String(20), default='normal')
    
    # status: issued, authorized, in progress, completed, canceled
    status = db.Column(db.String(20), default='issued')
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relación opcional para acceder a info del episodio si fuera necesario
    # episode = db.relationship("Episode", backref="orders")

    def to_dict(self):
        return {
            "id": self.id,
            "episode_id": self.episode_id,
            "type": self.type,
            "details": self.details, # SQLAlchemy lo convierte automáticamente a lista/dict de Python
            "priority": self.priority,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }