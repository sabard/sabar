from flask import escape, Flask, request, render_template, jsonify

app = Flask(__name__, static_url_path="")

@app.route('/')
def index():
    """Return the main page."""
    return render_template('index.html')


@app.route('/test', methods=['POST'])
def test():
    """Return a random prediction."""
    data = request.json
    return jsonify({'response': escape(data['user_input'])})