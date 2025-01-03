from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.sql import func

class Archive(db.Model):
    __tablename__ = "archives"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey("users.id"))
    url = db.Column(db.String, nullable=False)
    title = db.Column(db.String(25), nullable=False)
    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())

    user = db.relationship("User", back_populates="archives")
    sources = db.relationship("Sources", back_populates="archives")
