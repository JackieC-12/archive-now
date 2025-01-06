from app.models import db, Comment, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime


# Adds a demo user, you can add other users here if you want
def seed_comments():
    demoComment = Comment(
        userId=1, archiveId=2, message='First', created_at=datetime.now())
    marnieComment = Comment(
        userId=2, archiveId=1, message='No, I was first', created_at=datetime.now())
    bobbieComment = Comment(
        userId=3, archiveId=2, message="Hi, Im also here too", created_at=datetime.now())
    jackieComment = Comment(
        userId=4, archiveId=2, message='It is 1:36 AM I am losing it', created_at=datetime.now())
    jackieComment2 = Comment(
        userId=4, archiveId=2, message='AAAAAAAAAAA', created_at=datetime.now())

    db.session.add(demoComment)
    db.session.add(marnieComment)
    db.session.add(bobbieComment)
    db.session.add(jackieComment)
    db.session.add(jackieComment2)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_comments():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM comments"))

    db.session.commit()
