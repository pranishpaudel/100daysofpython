
from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"

near_value=[1,2,-1,-2]

@app.route('/guess/<unum>')
def guess_(unum):
    if int(unum)==random_number:
        return "<b>AHHHH!!! YOU GOT MEEEE!!!!!!"
    elif int(unum)-random_number in near_value:
        return "TOO NEAR!"
    elif int(unum)-random_number>0:
        return "TOO HIGH!"
    elif int(unum)-random_number<0:
        return "TOO LOW!"    





app.run(debug=True)