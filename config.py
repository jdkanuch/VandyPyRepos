# Basic configurations for the application
# Defines the DB path for dev and prod
# The GitHub API request is hardcoded for simplicity.

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' \
        + os.path.join(basedir, 'db/app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'df9f297d6ac73b3c39cf6860af969191'

    # GitHub API Query String
    GITHUB_API_STRING = 'https://api.github.com/search/repositories?q=language:python&sort=stars&order=des&per_page=5'

