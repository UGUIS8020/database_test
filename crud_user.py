from app import db, User, app
from datetime import datetime

with app.app_context():
    # user3 = User("test_user3@test.com","test_user3",datetime.strptime("2000-12-15", "%Y-%m-%d").date(),"female","1111")

    # db.session.add(user3)
    # db.session.commit()

    all_users = User.query.all()
    print(all_users)  

    userid_1 = User.query.get(1)
    print(userid_1.username)

    birth_users = User.query.filter_by(date_of_birth='2000-12-15').all()
    print(birth_users)

      # ユーザー名を更新
    userid_1.username = "test userA"
    db.session.add(userid_1)
    db.session.commit()

      # IDが2のユーザーを削除
    # userid_2 = User.query.get(2)
    # db.session.delete(userid_2)
    # db.session.commit()

    all_users = User.query.all()
    print(all_users)
