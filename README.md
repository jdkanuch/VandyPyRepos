# VandyPyRepos
VICTR Candidate Assessment. A basic Flask application using SQLAlchemy and the GitHub API to display the top 5 Python repositories with the most stars.

## Structure
### The main application modules are in /app.
- models.py
  - Defines the database model for the Repo class.
- routes.py
  - Handles the switching of views based on the routes.
    - home() returns a list of top Python repos and pushes it to the home.html template
    - refresh() calls refresh_repos() in the controller module and then redirects back to home() with updated repos and last-refreshed time.
- controller.py
  - Handles the back-end logic: querying the DB and calling the GitHub API.

### Templates and Static files
- /app/templates/base.html
  - This file contains the HTML headers and CDN links to the Bootstrap CSS and JS libraries and static CSS.
- /app/templates/home.html
  - Template for displaying the repository list returned from the route home() function.
- /app/templates/detail.html
  - Detailed information on 1 repository:
    - Repository ID
    - Name
    - URL
    - Description
    - Stars
    - Last pushed datetime
    - Created datetime

## Deployment

The app is [deployed to Google Cloud](http://victr-assessment-jkanuch.appspot.com/). 
It was developed using a SQLite3 database.

## Installation to run locally
_This assumes you have Python 3 installed and know how to setup a Python development environment using virtualenv._

_If not, see [this](https://cloud.google.com/python/setup) tutorial for setting one up._ 

1. Clone this repository. Change the directory to VandyPyRepos and setup and activate a virtualenv.
2. Run pip to install the project dependencies:
```
$ pip install -r requirements.txt
```
2. Run the following command to set the Flask application environment variable:
```
$ export FLASK_APP=pygit_agg.py
```
3. Run the following command to run the Flask application server locally:
```
$ flask run
```
4. Visit ```http://127.0.0.1:5000/``` in your browser.
