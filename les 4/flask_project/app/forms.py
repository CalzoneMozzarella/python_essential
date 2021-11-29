import flask_wtf
import wtforms
from wtforms.validators import DataRequired, Length, Email


class EnterNameForm(flask_wtf.FlaskForm):
    login = wtforms.StringField(label='Login:')
    password = wtforms.PasswordField(label='Password:', validators=[DataRequired(), Length(min=4, max=100)])
    submit = wtforms.SubmitField(label='Submit')
    add_user = wtforms.BooleanField(label='add_user')