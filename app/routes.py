from app import app
from flask import render_template, flash, redirect
from app.forms import RollDice
from app.roll import roll_em


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = RollDice()
    if form.validate_on_submit():
        flash('Rolling die {} with modifier {}'.format(
            form.die.data, form.mod.data))
        return roll_em(form.die.data, form.mod.data)

        # return redirect('/index')
    return render_template('roll.html', title='ROLL IT!', form=form)


