from app import app, forms
from flask import render_template, request, flash, redirect, url_for


@app.route('/')
@app.route('/index', methods=['GET','POST'])
def index():
    title = 'Login page'
    form = forms.LoginForm()

    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.login.data, form.password.data))
        return redirect(url_for('index'))

    data = request.form.get('login')
    # print(type(forms.LoginForm.submit))
    # print(type(data))
    # print(data)

    return render_template('index.html', title=title, form=form)

