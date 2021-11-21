import flask_wtf
import wtforms

class EnterNameForm(flask_wtf.FlaskForm):
    user_name = wtforms.StringField(label='Username')
    submit = wtforms.SubmitField(label='Submit')