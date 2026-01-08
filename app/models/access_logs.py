from app import db
from datetime import datetime

class AccessLog(db.Model):
    __tablename__ = 'access_logs'

    id = db.Column(db.Integer, primary_key=True)
    # foranean key a users.id
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True) # Puede ser NULL si es un intento de login fallido
    
    resource = db.Column(db.String(100), nullable=False) # Ej: /patients, /auth/login
    action = db.Column(db.String(100), nullable=False)   # Ej: GET, POST, DELETE, LOGIN
    ip_address = db.Column(db.String(45))                        # Soporta IPv4 e IPv6
    user_agent = db.Column(db.String(255))               # information of the client making the request
    details = db.Column(db.Text)                          # aditional details about the access event
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "resource": self.resource,
            "action": self.action,
            "ip_address": self.ip_address,
            "user_agent": self.user_agent,
            "details": self.details,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }