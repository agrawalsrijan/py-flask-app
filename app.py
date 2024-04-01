from flask import Flask
from routes.health import health_blueprint

app = Flask(__name__)

# register blueprints
app.register_blueprint(health_blueprint, url_prefix="/api/health")

if __name__ == "__main__":
    app.run(debug=True, port=3000)
