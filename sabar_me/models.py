from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from sabar_me import app

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# class Tag(db.Model):
#     __tablename__ = "tag"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)


# class Item(db.Model):
#     __tablename__ = "item"
#     id = db.Column(db.Integer, primary_key=True)


# class ItemTag(db.Model):
#     tag_id = db.Column(db.Integer)
#     item_id = db.Column(db.Integer)


# class Article(Item):
class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    text = db.Column(db.Text)
    # tags = db.Column(db.String)

def create_article(article_data, commit=True):
    article = Article(
        id=article_data.get("id"),
        title=article_data["title"],
        text=article_data["text"],
    )
    db.session.add(article)
    if commit:
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
    return article

class Image(db.Model):
    __tablename__ = "image"
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.Text)
