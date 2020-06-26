from app import app
from app import roll
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length
import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


class DiceForm(FlaskForm):
    die = StringField('dice to roll', [DataRequired()])
    mod = StringField('modifier')
    submit = SubmitField('Submit')


@app.route('/')
@app.route('/index')
def index():
    form = DiceForm()
    if form.validate_on_submit():
        print("yup")


@app.route('/dice')
def dice():
    # we are passing hard coded values for the dice and modifier, for now
    return str(roll.roll_em("6d20", "6"))
