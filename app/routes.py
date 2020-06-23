from app import app
from app import roll


@app.route('/')
@app.route('/index')
def index():
    return 'whoa!'


@app.route('/dice')
def dice():
    return str(roll.roll_em())
