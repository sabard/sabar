from flask import escape, request, render_template, jsonify
from flask_cors import CORS
from flask_graphql import GraphQLView

from . import app
from .graphql_schemas import schema

CORS(app)

@app.route('/')
def index():
    """Return the main page."""
    return render_template('index.html')


@app.route('/blog')
def blog():
    """Return the blog page."""
    return render_template('blog.html')

@app.route('/blog/<id>')
def blog_post(id):
    """Return a blog post view."""
    return render_template('blog_post.html')


@app.route('/portfolio')
def portfolio():
    """Return the portfolio page."""
    return render_template('portfolio.html')


@app.route('/photos')
def photos():
    """Return the photos page."""
    return render_template('photos.html')


@app.route('/audio')
def audio():
    """Return the audio page."""
    return render_template('audio.html')


@app.route('/test', methods=['POST'])
def test():
    """Return a random prediction."""
    data = request.json
    return jsonify({'response': escape(data['user_input'])})


def graphql_view():
    view = GraphQLView.as_view(
        "graphql", schema=schema, graphiql=True, batch=True
    )
    return view

app.add_url_rule("/graphql", view_func=graphql_view())
