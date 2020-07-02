from app import app
from flask import render_template
from app.forms import RollDice

@app.route('/')
@app.route('/index')
def index():
    # user = {'username': 'brad'}
    # return render_template('index.html', title='DICE', user=user)
    form = RollDice()
    return render_template('roll.html', title='ROLL', form=form)

