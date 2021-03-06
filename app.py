"""
Story Stack - Main flask app
"""

# pylint: disable=no-member
# pylint: disable=unused-import
import os
import re
import flask
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user,
)
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import find_dotenv, load_dotenv
from models import db, Account, Story, Like
from story import (
    post_story,
    parse_id,
    add_tags,
    get_displayable_stories,
    get_poster_username,
)
from search import search_db, get_query_tokens, search_children, search_liked


load_dotenv(find_dotenv())
app = flask.Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
DB_URL = os.getenv("DATABASE_URL")
if DB_URL.startswith("postgres://"):
    DB_URL = DB_URL.replace("postgres", "postgresql")
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

db.init_app(app)
with app.app_context():
    if __name__ == "__main__":
        db.create_all()

login_manager = LoginManager()
login_manager.login_view = "/login"
login_manager.login_message = ""
login_manager.init_app(app=app)


@login_manager.user_loader
def load_user(user_id):  # pylint: disable=missing-function-docstring
    return Account.query.get(int(user_id))


@app.route("/")
def main():
    """
    App route for users that aren't currently logged in.
    """
    if current_user.is_authenticated:
        return flask.redirect(flask.url_for("homepage"))
    return flask.render_template("index.html")


@app.route("/aboutus")
def aboutus():
    """
    App route for a small about us page.
    """
    return flask.render_template("aboutus.html")


@app.route("/info")
def info():
    """
    App route for a page containing information about the purpose
    of the app.
    """
    return flask.render_template("info.html")


@app.route("/home")
def homepage():
    """
    App route for the homepage of the application where users
    can access the application's functionality.
    """
    return flask.render_template("home.html")


@app.route("/signup", methods=["GET"])
def signup():
    """
    This route is the signup page for the applicaton. The user may only
    access this page if they are not currently logged in. If the user is
    logged in then they will be taken to the main page of the application.
    """
    if current_user.is_authenticated:
        return flask.redirect("/home")
    return flask.render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup_post():
    """
    This route accepts a post from the signup page to attempt to create a
    new user. If the username already exists then we flash a message to the
    user and refresh the page, otherwise we make create the user and redirect
    them to the login page.
    """
    email = flask.request.form.get("email").lower()
    username = flask.request.form.get("username").lower()
    password = flask.request.form.get("password")

    user = Account.query.filter_by(email=email).first()
    if user:
        flask.flash("Email already exists.")
        return flask.redirect("/signup")

    user = Account.query.filter_by(username=username).first()
    if user:
        flask.flash("Username already exists.")
        return flask.redirect("/signup")

    new_user = create_user(email, username, password)

    db.session.add(new_user)
    db.session.commit()
    flask.flash("Account created. Please login.")

    return flask.redirect("/login")


@app.route("/login", methods=["GET"])
def login():
    """
    This route is the login page for the application. The user may only
    access this page if they are not logged in. If the user is logged in
    then they will be taken to the main page of the application.
    """

    if current_user.is_authenticated:
        return flask.redirect("/")
    return flask.render_template("login.html")


@app.route("/login", methods=["POST"])
def login_post():
    """
    This route accepts a post from the login page to attempt to sign in the
    user based on their username and password. If the user has entered a
    valid username/password combo then they are logged in, otherwise they
    are flashed a message notifying them and the page is refreshed.
    """

    email = flask.request.form.get("email").lower()
    password = flask.request.form.get("password")

    user = Account.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flask.flash("Incorrect email or password.")
        return flask.redirect("/login")

    login_user(user, remember=True)
    # print(current_user.id)
    return flask.redirect("/home")


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    """
    This route logs out the user and redirects them to index page.
    """
    logout_user()
    return flask.redirect("/")


@app.route("/profile", methods=["GET"])
@login_required
def profile():
    """
    This route is the profile page for the currently logged in user. The
    page currently uses React to load the user's written reviews and allow
    them to modify their rating or delete comments.
    """
    return flask.render_template("profile.html")


@app.route("/story", methods=["GET"])
def story():
    """
    This route is the route to view a single story page.
    """
    story_id = flask.request.args.get("story_id")
    if not story_id:
        story_id = 0
    story_id = parse_id(story_id)
    curr_story = Story.query.filter_by(id=story_id).first()
    child_titles, child_texts, child_ids = search_children(story_id)
    if curr_story:
        return flask.render_template(
            "story.html",
            poster_name=get_poster_username(curr_story),
            title=curr_story.title,
            text=curr_story.text,
            story_id=curr_story.id,
            child_titles=child_titles,
            child_texts=child_texts,
            child_ids=child_ids,
        )

    return flask.render_template("story.html")


@app.route("/post", methods=["GET"])
@login_required
def post_form():
    """
    This route is for the posting page of stories. The parent of the story
    being written is a parameter in the URL. If there is no parent story then
    the default id is currently -1 for root stories.
    """
    parent_id = flask.request.args.get("parent")
    if not parent_id:
        parent_id = -1
    return flask.render_template("post.html", parent_id=parent_id)


@app.route("/post", methods=["POST"])
@login_required
def post():
    """
    This is the route for posting stories. Once the story has been posted
    the user will be redirected to a page to view the new story.
    """
    parent = flask.request.args.get("parent")
    userid = current_user.id
    text = flask.request.form.get("text")
    title = flask.request.form.get("title")
    tags = get_query_tokens(flask.request.form.get("tags"))
    new_story = Story(
        parent=parent,
        userid=userid,
        text=text,
        title=title,
    )
    if post_story(new_story):
        add_tags(new_story, tags)

    return flask.redirect("/story?story_id=" + str(new_story.id))


@app.route("/orphan", methods=["POST"])
@login_required
def orphan():
    """
    This is the app route so that users can remove their assosiated
    with previously written stories.
    """
    storyid = flask.request.form.get("id")
    story_obj = Story.query.filter_by(id=storyid).first()
    story_obj.userid = None
    db.session.commit()
    return flask.redirect("/")


@app.route("/search", methods=["GET"])
@login_required
def search_get():
    """
    This is the app route for the search page. The user can currently
    pass a query that will be used to search for stories that match either
    a stories tag or id.
    """
    query = flask.request.args.get("query")
    matching_stories = search_db(query)
    stories = get_displayable_stories(matching_stories)

    return flask.render_template("search.html", query=query, stories=stories)


@app.route("/view_liked", methods=["GET"])
@login_required
def view_liked():
    """
    App route to view stories that the user has liked/bookmarked.
    """
    liked_titles, liked_texts, liked_ids = search_liked(current_user.id)
    return flask.render_template(
        "bookmarks.html",
        liked_titles=liked_titles,
        liked_ids=liked_ids,
        liked_texts=liked_texts,
    )


def create_user(email: str, username: str, password: str) -> Account:
    """
    Takes in a user's email, username, and password and returns a new Account
    object if all the fields are valid. This function should be run after the
    username and email have been checked for uniqueness.

    Args:
        email (str): The user's email.
        username (str): The user's username.
        password (str): The user's password.

    Returns:
        Account: An account object representing the new user.
    """
    regex = r"^[0-9a-zA-Z]+\.?[0-9a-zA-Z]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$"
    if (not (email and username and password)) or (not re.fullmatch(regex, email)):
        return None
    new_user = Account(
        email=email,
        username=username,
        password=generate_password_hash(password, method="sha256"),
    )
    return new_user


if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),  # pylint: disable=invalid-envvar-default
        debug=True,
    )
