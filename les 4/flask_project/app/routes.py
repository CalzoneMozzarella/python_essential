from app import app, forms
from flask import render_template


@app.route('/')
@app.route('/index', methods=['POST'])
def index():
    title = 'Login page'
    form =forms.EnterNameForm()
    return render_template('index.html', title=title, form=form)
