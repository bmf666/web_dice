from app import app

@app.route('/')
@app.route('index')
def index():
    return '\n\n\n\whoa!'
