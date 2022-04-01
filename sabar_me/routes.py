from flask import escape, request, render_template, jsonify

from . import app


@app.route('/')
def index():
    """Return the main page."""
    return render_template('index.html')


@app.route('/blog')
def blog():
    """Return the blog page."""
    return render_template('blog.html')


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
