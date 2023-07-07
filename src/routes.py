from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from src import app, db
from src.forms import LoginForm, RegisterForm, SearchArticles
from src.models import Users


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/articles_extractor_str/")
@login_required
def articles_extractor_str():
    return render_template("articles_extractor_str.html")


@app.route("/articles_extractor/")
@login_required
def articles_extractor():
    form = SearchArticles()
    return render_template("articles_extractor.html", form=form)


@app.route("/register/", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = Users(
            name=form.name.data, email=form.email.data, password_cryp=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("articles_extractor"))
    if form.errors != {}:
        for err in form.errors.values():
            flash(f"Error user register {err}", category="danger")
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_logged = Users.query.filter_by(email=form.email.data).first()
        if user_logged and user_logged.convert_password(
            password_clean_text=form.password.data
        ):
            login_user(user_logged)
            flash(f"Success! Your login is: {user_logged.name}", category="success")
            return redirect(url_for("articles_extractor"))
        else:
            flash(f"User or password it's wrong. Try again!", category="danger")
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    flash("You do logout", category="info")
    return redirect(url_for("home"))