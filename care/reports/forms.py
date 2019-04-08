from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired


class ReportForm(FlaskForm):
    user_id  =StringField('User Id', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    picture = FileField('Add Report', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField("AddIn")
