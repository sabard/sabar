from flask import escape, request, render_template, jsonify
from flask_cors import CORS
from flask_graphql import GraphQLView

from . import app
from .graphql_schemas import schema
from .models import get_project, get_projects, Category


CORS(app)

@app.route("/")
def index():
    """Return the main page."""
    return render_template("index.html")


@app.route("/about")
def about():
    """Return the main page."""
    return render_template("about.html")

@app.route("/articles")
def articles():
    """Return the articles page."""
    return render_template("articles.html")

@app.route("/articles/<article_id>")
def article(article_id):
    """Return the article view."""
    return render_template("article.html", article_id=article_id)


@app.route("/projects")
def projects():
    """Return the projects page."""
    projects = get_projects()
    tools = [p for p in projects if p.category == Category.tool]
    builds = [p for p in projects if p.category == Category.build]

    return render_template("projects.html", tools=tools, builds=builds)


@app.route("/project/<project_slug>")
def project(project_slug):
    """Return the project view."""
    project = get_project(project_slug)
    return render_template("project.html", project=project)

@app.route("/photos")
def photos():
    """Return the photos page."""
    return render_template("photos.html")


@app.route("/audio")
def audio():
    """Return the audio page."""
    return render_template("audio.html")


@app.route("/test", methods=["POST"])
def test():
    """Return a random prediction."""
    data = request.json
    return jsonify({"response": escape(data["user_input"])})


def graphql_view():
    view = GraphQLView.as_view(
        "graphql", schema=schema, graphiql=True, batch=True
    )
    return view

app.add_url_rule("/graphql", view_func=graphql_view())
