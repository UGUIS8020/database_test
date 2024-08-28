from app import db, BlogPost, app

with app.app_context():
    
 # 既存のデータを消去
    BlogPost.query.delete()

    blog_post1 = BlogPost(1,
   "ブログテスト", "こちらはブログの書き込みテスト用のサンプル文章です。この文章は、システムの動作確認やレイアウトの確認を目的として使用されます。ブログの内容や見栄えをテストする際に、この文章を使って、実際の投稿がどのように表示されるかを確認してください。内容は特に意味を持たず、文字数を150文字に調整しています。", "summary1", "featured_image1")
    blog_post2 = BlogPost(1, "title2", "text2,text2,text2", "summary2", "featured_image2")
    blog_post3 = BlogPost(3, "title3", "text3,text3,text3", "summary3", "featured_image3")
    blog_post4 = BlogPost(3, "title4", "text4,text4,text4", "summary4", "featured_image4")

    db.session.add_all([blog_post1,blog_post2,blog_post3,blog_post4])

   #  db.session.add(blog_post4)
    db.session.commit()

