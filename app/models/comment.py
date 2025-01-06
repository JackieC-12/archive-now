from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Comment(db.Model):
    __tablename__ = "comments"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey("users.id"))
    archiveId = db.Column(db.Integer, db.ForeignKey("archives.id"))
    message = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.now(tz=None))

    user = db.relationship("User", back_populates="comments")
    archive = db.relationship("Archive", back_populates="comments")
