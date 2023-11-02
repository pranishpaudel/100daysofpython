from flask import Flask
from flask import render_template
from blog import Blog
app = Flask(__name__)


blog= Blog()
@app.route('/')
def hello_world():
    return render_template("index.html",data=blog.return_all_info())


@app.route("/about.html")
def about_info():
    return render_template("about.html")

@app.route("/contact.html")
def contact_info():
    return render_template("contact.html")

@app.route("/post.html")
def post_info():
    return render_template("post.html")


@app.route("/postinfo.html/<num>")
def info_post(num):
    send_info= blog.return_specific(int(num))
    return render_template("post_info.html",info=send_info)

app.run(debug=True)