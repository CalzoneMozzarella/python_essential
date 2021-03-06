from app import app, forms
from flask import render_template, request, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from flask import request
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    title = 'index'
    form = forms.LoginForm()

    return render_template('index.html', title=title, form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    title = 'Login page'
    form = forms.LoginForm()

    # u = User(username='Irina_1959', email='Irina_1959@example.com')
    # u.set_password('123456')


    if form.validate_on_submit():
        user = User.query.filter_by(username=form.login.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    # data = request.form.get('login')
    # print(type(forms.LoginForm.submit))
    # print(type(data))
    # print(data)

    return render_template('login.html', title=title, form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
