from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from forms import RegistrationForm, CollectionForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secure secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_url'  # Example: 'postgresql://username:password@localhost/dbname'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)

from models import User, Collection

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('register.html', form=form)

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    form = CollectionForm()
    if form.validate_on_submit():
        item = Collection(
            name=form.name.data,
            description=form.description.data
        )
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_item.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)