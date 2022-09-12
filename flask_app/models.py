from flask_app import db
from datetime import datetime


class User(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(20), unique=True, nullable=False)
    last_name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    post = db.relationship('Recipe', backref='chef', lazy=True)

    def __repr__(self) -> str:
        return f"User('{self.username}', '{self.email}')"

class Recipe(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text(100), nullable=False)
    instructions = db.Column(db.Text(100), nullable=False)
    date_cooked = db.Column(db.DateTime, nullable=False, default=datetime.utcnow )
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self) -> str:
        return f"Recipe('{self.recipe_name}','{self.description}','{self.instructions}','{self.date_cooked}')"