from app import app
from app import roll


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'brad'}
    return '''
<html>
    <head>
        <title>Dice roll!</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
        <h1> ''' + str(roll.roll_em("6d20", "12")) + ''' </h1>
    </body>
</html>'''
