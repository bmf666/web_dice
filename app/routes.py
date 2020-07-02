from app import app
from flask import render_template
from app.forms import RollDice


@app.route('/')
@app.route('/index')
def index():
    form = RollDice()
    return render_template('roll.html', title='ROLL', form=form)
