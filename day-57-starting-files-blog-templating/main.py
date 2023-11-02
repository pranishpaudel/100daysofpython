from flask import Flask, render_template
from post import Post


app = Flask(__name__)
post= Post()

@app.route('/')
def home():
    return render_template("index.html",posts=post.send_all_post())

@app.route('/post/<num>')
def get_post(num):
    print(num)
    return render_template("post.html",posts=post.
                           
                           send_wanted_post(int(num)))




if __name__ == "__main__":
    app.run(debug=True)
