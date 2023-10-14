from flask import Flask, render_template
from random import randint
from datetime import datetime
import requests

app = Flask(__name__)



def get_data_by_name(name):
    data= requests.get(f"https://api.agify.io/?name={name}").json()
    guessed_age= data["age"]
    return guessed_age


# print(get_data_by_name("pranish"))


@app.route('/<namee>')
def home(namee):
    random_num= randint(0,10)
    current_year= datetime.now().year
    return render_template("index.html",numm=random_num,year=current_year,age=get_data_by_name(namee),name=namee)


if __name__ == "__main__":
    app.run(debug=True)


