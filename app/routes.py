# This module defines the home and detail views
# This module also defines the route for calling the GitHub API (refresh())

from flask import render_template, redirect, url_for, session
from app import app
from app.controller import refresh_repos, get_repo_list, get_repo_details


@app.route('/')
def home():
    repos = get_repo_list()
    return render_template("home.html", repos=repos)


@app.route('/refresh')
def refresh():
    update_time = refresh_repos()
    session['messages'] = update_time
    return redirect(url_for('home'))


@app.route('/repo/<int:repo_id>')
def detail(repo_id):
    repo = get_repo_details(repo_id)
    return render_template("detail.html", repo=repo)
