from portfolio import db, login_manager
from flask_login import UserMixin

'''
Each project include a title, breif 
and long descriptions, screenshots, 
key features, tags of technologies/packages used, link to github source repo
'''
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    short_desc = db.Column(db.String(200), nullable=False)
    long_desc = db.Column(db.String(500), nullable=False)
    features = db.Column(db.String(120), nullable=False)
    tags = db.Column(db.String(120), nullable=False)
    user_id =  db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Creating User models
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    projects = db.relationship('Project', backref='author', lazy=True)

    #This is the representation of a User 
    def __repr__(self):
        return f"User('{self.username}')"

# This function is used to manage user login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


