from app import app
from flask import render_template, flash, redirect
from app.forms import RollDice
from app.roll import roll_em


@app.route('/')
@app.route('/index')
def index():
    form = RollDice()
    return render_template('roll.html', title='ROLL', form=form)


@app.route('/roll', methods=['GET', 'POST'])
def roll():
    form = RollDice()
    if form.validate_on_submit():
        flash('Rolling die {} with modifier {}'.format(
            form.die.data, form.mod.data))
        roll_results = roll_em(form.die.data, form.mod.data)
        form.results.data

        return redirect('/roll')
    return render_template('roll.html', title='ROLL IT!', form=form)
