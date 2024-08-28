from app import db, User, BlogPost, app


with app.app_context():
    all_posts = BlogPost.query.all()
    print(all_posts)