from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    blog_urll= "https://api.npoint.io/126573c3358ffdf5c119"
    response= requests.get(blog_urll)
    all_posts= response.json()
    return render_template("index.html",posts=all_posts)




if __name__ == "__main__":
    app.run(debug=True)
