from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Archive(db.Model):
    __tablename__ = "archives"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey("users.id"))
    url = db.Column(db.String, nullable=False)
    title = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String)
    fileLink = db.Column(db.String)

    user = db.relationship("User", back_populates="archives")


    # user = db.relationship("User", back_populates="archives")
    # sources = db.relationship("Sources", back_populates="archives")
