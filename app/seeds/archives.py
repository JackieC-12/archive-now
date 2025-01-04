from app.models import db, Archive, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_archives():
    demoArchive = Archive(
        userId=1, url='https://knowyourmeme.com', title='know your meme', description='example description')
    marnieArchive = Archive(
        userId=2, url='https://warframe.com', title='Warframe website', description='Warframe website')
    bobbieArchive = Archive(
        userId=3, url='https://store.steampowered.com/', title='Steam website', description='I am going to die')

    db.session.add(demoArchive)
    db.session.add(marnieArchive)
    db.session.add(bobbieArchive)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_archives():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM archives"))

    db.session.commit()
