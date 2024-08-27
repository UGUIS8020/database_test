from app import db, User, app
from datetime import datetime


with app.app_context():

    db.create_all()

    user1 = User("test_user1@test.com","test_user1",datetime.strptime("1999-01-01", "%Y-%m-%d").date(), "male","1111")
    user2 = User("test_user2@test.com","test_user2",datetime.strptime("1980-01-01", "%Y-%m-%d").date(),"female","1111")

    db.session.add_all([user1, user2])

    db.session.commit()

    print(user1.id)
    print(user2.id)