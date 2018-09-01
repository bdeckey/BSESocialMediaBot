from flask import render_template, flash, redirect, request, url_for
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.urls import url_parse
from datetime import datetime
from socialmediabot import app, db
from socialmediabot.models import User
from socialmediabot.forms import LoginForm, RegistrationForm, EditProfileForm

@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit(): #always returns false for GET

        # 1. get the user object by querying db for username
        user = User.query.filter_by(username = form.username.data).first()
        print(user)
        # 2. check if the user does not exist or if password is incorrect
        if user is None or not user.check_password(form.password.data):
            print("invalid")
            flash("Invalid username or password")
            return redirect(url_for("login"))

        # 3. since username/password are valid, log in the user
        print("logging in!")
        login_user(user, remember = form.remember_me.data)

        # 4. if next_page query param from @login_required,
        # redirect to potential page user was trying to get to before
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).decode_netloc() != "":
            next_page = url_for("home")
        print(next_page)
        return redirect(next_page)

    return render_template("login.html", title="Login :)", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email = form.email.data, about_me = form.about_me.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for("login"))
    return render_template("register.html", title = "Register", form = form)

@app.route("/home")
@login_required
def home():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("home.html", title="Home Page", posts=posts)

@app.route("/user/<username>")
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template("user.html", user=user, posts=posts)

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    print(form.validate_on_submit())
    print(form.username.data)
    print(form.about_me.data)

    if form.validate_on_submit():
        print("submitted")
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)

# @app.route("/edit_profile", methods = ["GET", "POST"])
# @login_required
# def edit_profile():
#     form = EditProfileForm()
#     if form.validate_on_submit():
#         current_user.username = form.username.data
#         current_user.password = form.password.data
#         current_user.about_me = form.about_me.data
#         db.session.commit()
#         flash('Your changes have been saved.')
#         return redirect(url_for('edit_profile'))
#     elif request.method == "GET":
#         form.username.data = current_user.username
#         form.about_me.data = current_user.about_me
#     return render_template('edit_profile.html', title='Edit Profile',
#                            form=form)
@app.route("/contact")
@login_required
def contact():
    print()

@app.route("/about")
@login_required
def about():
    print()

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return(redirect(url_for("login")))

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()