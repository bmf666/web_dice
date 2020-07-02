from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class RollDice(FlaskForm):
    die = StringField('Die')
    mod = StringField('modifier')
    submit = SubmitField('Roll!')