from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, URL, Optional


class PostForm(FlaskForm):
    body = StringField('Body', validators=[DataRequired()])
    url = URLField('URL', validators=[Optional(), URL()])
    submit = SubmitField('Post')
