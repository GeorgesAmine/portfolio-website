from flask import render_template, redirect, url_for, request, flash
from portfolio import app, db, bcrypt
from portfolio.models import Project, User
from portfolio.forms import LoginForm
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/project/<project_id>")
def project(project_id):
    project_id=project_id
    return render_template("project.html", project_id=project_id)

# Login route
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        print(current_user)
        return redirect(url_for('home'))
    # Creating form based on imported LoginForm
    form = LoginForm()
    if form.validate_on_submit():
        # if valid entries then check for authorised access
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
        else:
            #if not authorized then flash danger and check credentials msg
            flash('Login unsuccessful, Please check email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/admin")
@login_required
def admin():
    return render_template("admin.html")