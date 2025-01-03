from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.sql import func

class Source(db.Model):
    __tablename__ = "sources"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    archiveId = db.Column(db.Integer, db.ForeignKey("archives.id"))
    fileLink = db.Column(db.String, nullable=False)
    rawHTML = db.Column(db.String, nullable=False)
    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())


    archive = db.relationship("Archive", back_populates="archives")
    