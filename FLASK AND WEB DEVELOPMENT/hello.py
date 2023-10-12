from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/bye')
def bye():
    return "BYW!!!!!"


@app.route('/username/<user>/<int:number>')
def heelllo(user,number):
    return f"Hello there {user} with number {number}"

if __name__ == '__main__':
    app.run(debug=True)
