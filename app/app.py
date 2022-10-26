from flask import Flask
from app.handlers.routes import configure_routes

app = Flask(__name__)

configure_routes(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=80)
