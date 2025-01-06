from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

class EditArchiveForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    description = StringField('description')
    submit = SubmitField('Submit')
