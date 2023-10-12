from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1 style="text-align: center">Hello, World!</h1><p>This is paragraph</p>'

def make_bold(function):
    def bold():
       return f"<b>{function()}</b>"
    return bold

def make_emphasis(function):
    def bold():
       return f"<em>{function()}</em>"
    return bold

@app.route('/bye')
@make_bold
@make_emphasis
def bye():
    return "BYW!!!!!"


@app.route('/username/<user>/<int:number>')
def heelllo(user,number):
    return f"Hello there {user} with number {number}"

if __name__ == '__main__':
    app.run(debug=True)
