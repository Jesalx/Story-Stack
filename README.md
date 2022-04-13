# Story Stack

[Sprint 1 Deployment](https://story-stack-gsu.herokuapp.com/)

[Sprint 2 Deployment](https://gsu-story-stack.herokuapp.com)

This project's aim is to deliver a collaborative story building web application. One of the primary goals of our is to create an experience similar to the ["exquisite corpse" concept](https://en.wikipedia.org/wiki/Exquisite_corpse) where collaboration is the focus.

The web app is built using [Flask](https://flask.palletsprojects.com/) in the backend, HTML/JS in the frontend, [PostgreSQL](https://www.postgresql.org/) for the database, [Flask-Login](https://flask-login.readthedocs.io/en/latest/) for authentication, and [Heroku](https://www.heroku.com/) for deployment.

## Installation Instructions

The first step to installation is going to be downloading the necessary files. If you wish to clone the repo you can do so by following [Github's documented instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

Inside the directory you will need to create a file named `.env`. Inside the file should be two lines in the following format:

```text
DATABASE_URL = "YOUR_DATABASE_URL"
SECRET_KEY = "YOUR_SECRET_KEY
```

where ```YOUR_DATABASE_URL``` is the url to your postgresql database that starts with ```postgresql://```, and ```YOUR_SECRET_KEY``` is a secret key that you have created.

Now that you have the right items inside of `.env` in the correct format you'll need to make sure that you have the correct packages installed for Python to run the project. To do this you can look inside the `requirements.txt` file and install each of the named packages individually, or run the command

```pip install -r requirements.txt```

Once you have all of the packages downloaded you are able to run the app with

```python app.py```
