from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class RollDice(FlaskForm):
    die = StringField('Die')
    mod = StringField('Modifier')
    submit = SubmitField('Roll!')