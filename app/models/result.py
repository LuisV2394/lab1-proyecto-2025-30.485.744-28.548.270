from app import db
from datetime import datetime

class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    summary = db.Column(db.Text, nullable=False)
    file_id = db.Column(db.String(255))
    version = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    order = db.relationship("Order", backref="results")

    def to_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "date": self.date.isoformat(),
            "summary": self.summary,
            "file_id": self.file_id,
            "version": self.version,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }