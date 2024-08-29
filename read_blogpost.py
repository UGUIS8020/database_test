from app import db, User, BlogPost, app


with app.app_context():
    all_posts = BlogPost.query.all()
    all_posts = User.query.all()
    print(all_posts)