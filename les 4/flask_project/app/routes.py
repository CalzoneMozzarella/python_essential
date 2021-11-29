from app import app, forms
from flask import render_template, request


@app.route('/')
@app.route('/index', methods=['GET','POST'])
def index():
    title = 'Login page'
    form = forms.EnterNameForm()

    data = request.form.get('user_name')
    print(type(data))
    print(data)

    return render_template('index.html', title=title, form=form)

