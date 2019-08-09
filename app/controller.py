# This module manages the back-end logic of the application

import requests
from config import Config
from app.models import Repo, db
from datetime import datetime


def refresh_repos():
    """ Calls the GitHub API and writes to the db with the top-starred repos."""
    try:
        # Call GitHubs API, the query params are set in Config
        response = requests.get(Config.GITHUB_API_STRING)

        # clear table and repopulate if response exists
        if response.status_code == 200:
            db.drop_all()
            db.create_all()

            for repo in response.json()['items']:
                new_repo = Repo(
                    id=repo['id'],
                    name=repo["name"],
                    url=repo["html_url"],
                    description=repo["description"],
                    star_count=repo["stargazers_count"],
                    created_date=repo["created_at"],
                    last_push_date=repo["pushed_at"],
                    modify_dtm=datetime.now(),
                )

                # Insert record
                db.session.add(new_repo)
                db.session.commit()

    finally:
        # Would ideally want to add more exception handling here.
        pass

    # This extra query returns the most recent db timestamp
    refresh_time = Repo.query.order_by(Repo.modify_dtm.desc()).first().modify_dtm
    return refresh_time.split(".")[0]


def get_repo_list():
    """This call to the DB returns the list of repositories stored from refresh_repos() """
    repos = Repo.query.order_by(Repo.star_count.desc()).all()
    return repos


def get_repo_details(repo_id):
    """Queries the DB for the given repo_id"""
    repo = Repo.query.filter_by(id=repo_id).one()
    return repo
