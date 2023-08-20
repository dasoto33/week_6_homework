from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secure secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_url'  # Example: 'postgresql://username:password@localhost/dbname'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes  # Import the routes module after creating the app and database instances