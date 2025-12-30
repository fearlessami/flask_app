# app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to my Flask app!</h1>'

@app.route('/about')
def about():
    return '<h2>About Page</h2><p>This is a simple Flask example.</p>'

@app.route('/hello/<name>')
def hello(name):
    return f'<h1>Hello, {name.capitalize()}!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
