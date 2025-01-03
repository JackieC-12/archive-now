from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

class ArchiveForm(FlaskForm):
    url = StringField(
        'Website URL', validators=[DataRequired(), URL()]
    )
    title = StringField('Archive Name', validators=[DataRequired()])
    description = StringField('Description of Archive')
    submit = SubmitField('Submit')
