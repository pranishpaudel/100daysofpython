from flask import Flask, render_template, redirect, url_for,request,jsonify
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/air/Desktop/100daysofpython/day-67-starting-files-upgraded-blog/instance/posts.db'
ckeditor = CKEditor(app)
db = SQLAlchemy()
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


with app.app_context():
    db.create_all()


def get_all_post():
    with app.app_context():
        all_postss= BlogPost.query.all()
        return (all_postss)
@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = []
    return render_template("index.html", all_posts=get_all_post())

# TODO: Add a route so that you can click on individual posts.
@app.route('/<post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    with app.app_context():
        requested_post=BlogPost.query.get_or_404(post_id)
    return render_template("post.html", post=requested_post)


@app.route("/new-post",methods=["POST","GET"])
def create_new_post():
    form= CreatePostForm()
    if request.method=="POST":
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=form.author.data,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return render_template("index.html")

    
    return render_template("make-post.html",form=form)

# TODO: add_new_post() to create a new blog post

@app.route("/new-post/<id>",methods=["POST","GET"])
def update_blod(id):
    form=CreatePostForm()
    if request.method=="POST":
        current_blog= BlogPost.query.get_or_404(id)
        current_blog.title=form.title.data
        current_blog.subtitle=form.subtitle.data
        current_blog.author= form.author.data
        current_blog.date= date.today().strftime("%B %d, %Y")
        current_blog.body= form.body.data
        current_blog.img_url= form.img_url.data
        insa= db.session.commit()
        if current_blog.title==form.title.data:
            return jsonify({"Success": "The blog was updated successfully"}),200
    


    return render_template("make-post.html",form=form)
  

# TODO: delete_post() to remove a blog post from the database
@app.route("/delete/<id>")
def delete_post(id):
    with app.app_context():
        blog_to_delete= BlogPost.query.get_or_404(id)
        db.session.delete(blog_to_delete)
        final_thing= db.session.commit()
        if final_thing=="None":
            return "DELETED SUCCESSFULLY"
# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
