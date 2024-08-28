from app import db, User, BlogPost, app

with app.app_context():
    # 新しいユーザーを追加
    user = User(email="test@example.com", username="testuser", date_of_birth="1990-01-01", gender="M", password_hash="hashedpassword", administrator="N")
    db.session.add(user)
    db.session.commit()

    # 新しいブログ投稿を追加
    blog_post = BlogPost(user_id=user.id, title="Test Post", text="This is a test post", summary="Test Summary", featured_image="image.jpg")
    db.session.add(blog_post)
    db.session.commit()

    # リレーションシップの確認
    print(user.posts.all())