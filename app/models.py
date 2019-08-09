# This module sets up the Repo class

from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)


class Repo(db.Model):

    __tablename__ = 'repositories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    url = db.Column(db.String(250))        # html_url
    created_date = db.Column(db.String(25))       # "created_at": "2018-07-05T09:11:43Z"
    last_push_date = db.Column(db.String(25))     # "pushed_at": "2019-06-08T14:57:19Z"
    description = db.Column(db.Text)            # description
    star_count = db.Column(db.Integer)          # stargazers_count
    modify_dtm = db.Column(db.String(25))

    def __repr__(self):
        return f"({name}, {url})"

