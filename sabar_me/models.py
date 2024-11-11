import enum

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from slugify import slugify
from sqlalchemy import Enum

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


"""Article"""

def db_commit():
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

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


"""Image"""

class Image(db.Model):
    __tablename__ = "image"
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.Text)


"""Project"""

class Category(enum.Enum):
    tool = 1
    build = 2

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String, nullable=False)
    category = db.Column(db.Enum(Category))
    subcategory = db.Column(db.String)
    title = db.Column(db.String)
    text = db.Column(db.Text)
    image_link = db.Column(db.String)

def create_project(project_data, commit=True):
    project = Project(
        id=project_data.get("id"),
        slug=slugify(project_data["title"]),
        category=project_data["category"],
        subcategory=project_data["subcategory"],
        title=project_data["title"],
        text=project_data["text"],
        image_link=project_data["image_link"]
    )
    db.session.add(project)
    if commit:
        db_commit()
    return project

def update_project(project_id_or_slug, project_data, commit=True):
    project = get_project(project_id_or_slug)
    for key, value in project_data.items():
        setattr(project, key, value)
    if commit:
        db_commit()
    return project

def get_projects():
    return db.session.query(Project).all()

def get_project(id_or_slug):
    if isinstance(id_or_slug, int):
        return db.session.query(Project).get(id_or_slug)
    else:
        return db.session.query(Project).filter_by(slug=id_or_slug).first()

def delete_project(project_id, commit=True):
    project = db.session.query(Project).filter_by(id=project_id)
    project.delete()
    if commit:
        db_commit()
    return project
