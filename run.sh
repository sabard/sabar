set -a && . ./variables-dev.env && set +a
gunicorn --bind 0.0.0.0:5000 sabar_me:app
