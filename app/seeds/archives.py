from app.models import db, Archive, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_archives():
    demoArchive = Archive(
        userId=1, url='https://knowyourmeme.com', title='know your meme', description='example description', fileLink='https://archive-now-bucket-pdf.s3.us-east-1.amazonaws.com/ea97ed2280b34552bff9388f8b96d380.pdf')
    marnieArchive = Archive(
        userId=2, url='https://warframe.com', title='Warframe website', description='Warframe website', fileLink='http://archive-now-bucket-pdf.s3.amazonaws.com/53e8649d9062492b860c4416177c5c1f.pdf')
    bobbieArchive = Archive(
        userId=3, url='http://www.onemorelevel.com/', title='Onemorelevel', description='I am going to die', fileLink='http://archive-now-bucket-pdf.s3.amazonaws.com/fdf86ad22dce49f5ab4fbdc62e0a567d.pdf')
    jackieArchive = Archive(
        userId=3, url='https://steamcommunity.com/', title='Steam community website', description='I am going to die 2', fileLink='https://archive-now-bucket-pdf.s3.us-east-1.amazonaws.com/5bbaa5fc51ff4098bd374292f2b2d9fd.pdf')
    jackieArchive2 = Archive(
        userId=3, url='https://www.spacejam.com/1996/', title='Steam community website', description='I am going to die 2', fileLink='http://archive-now-bucket-pdf.s3.amazonaws.com/5f6be3ab433b487ea325e91576ba06eb.pdf')


    db.session.add(demoArchive)
    db.session.add(marnieArchive)
    db.session.add(bobbieArchive)
    db.session.add(jackieArchive)
    db.session.add(jackieArchive2)
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
