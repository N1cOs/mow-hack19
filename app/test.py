from app.app import app


@app.route('/')
def hello():
    return 'hello!'
