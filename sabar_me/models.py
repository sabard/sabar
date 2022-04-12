from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from sabar_me import app

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    text = db.Column(db.Text)

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
