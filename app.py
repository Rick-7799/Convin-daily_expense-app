from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from routes import routes_app  # Import the routes blueprint

# Initialize the database
db = SQLAlchemy()

# Create the Flask application
app = Flask(__name__)

# Configure the database URI and JWT settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret

# Initialize the database and JWT manager
db.init_app(app)
jwt = JWTManager(app)

# Create database tables if they don't exist
with app.app_context():
    db.create_all()

# Register the routes blueprint
app.register_blueprint(routes_app)

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(e):
    return jsonify(error="Resource not found"), 404

# Test route to check if the server is running
@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "Server is running!"}), 200

if __name__ == '__main__':
    app.run(debug=True)