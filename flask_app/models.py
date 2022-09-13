from flask_app import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id =db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(20), unique=True, nullable=False)
    last_name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    post = db.relationship('Recipe', backref='chef', lazy=True)
    # image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    def __repr__(self) -> str:
        return f"User('{self.username}','{self.first_name}','{self.last_name}', '{self.email}')"

class Post(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text(100), nullable=False)
    instructions = db.Column(db.Text(100), nullable=False)
    date_cooked = db.Column(db.DateTime, nullable=False, default=datetime.utcnow )
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self) -> str:
        return f"Recipe('{self.recipe_name}','{self.description}','{self.instructions}','{self.date_cooked}')"