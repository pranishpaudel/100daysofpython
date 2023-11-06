from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

##CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/air/Desktop/100daysofpython/day-64-starting-files-top-movies/dbnew.db'
db = SQLAlchemy()
db.init_app(app)


##CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

class MyForm(FlaskForm):
    movie = StringField('Movie', validators=[DataRequired("Please enter the movie name.")])
    submit = SubmitField('Submit')

with app.app_context():
    db.create_all()

## After adding the new_movie the code needs to be commented out/deleted.
## So you are not trying to add the same movie twice. The db will reject non-unique movie titles.
def create_new_row():
    new_movie = Movie(
    title="Avatar The Way of Water",
    year=2022,
    description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    rating=7.3,
    ranking=9,
    review="I liked the water.",
    img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
    )


    with app.app_context():
        db.session.add(new_movie)
        db.session.commit()

create_new_row()
def return_all_records():
    with app.app_context():
        all_movies= Movie.query.all()
        return all_movies



@app.route("/")
def home():
    return render_template("index.html",all_movies=return_all_records())

def get_moviue_by_primary(num,newrate,newreview):
    with app.app_context():
        movie_name= db.get_or_404(Movie,num)
        movie_name.rating=newrate
        movie_name.review=newreview
        done= db.session.commit()
        return done
    
def delete_moviue_by_primary(num):
    with app.app_context():
        movie_name= db.get_or_404(Movie,num)
        db.session.delete(movie_name)
        all_movies= Movie.query.all()
        countt=1
        for movie in all_movies:
            movie.id= countt
            countt+=1


        done= db.session.commit()
        return done


@app.route("/edit/<insa>",methods=["POST","GET"])
def edit_it(insa):
    current_id=insa


    if request.method=="POST":
        userrating= request.form["rating"]
        userreview= request.form["review"]
        print(current_id)
        error_rate= str(get_moviue_by_primary(current_id,float(userrating),userreview))
        if error_rate.lower()=="none":
            return "Changed succesfully"
    
    return render_template("edit.html")

@app.route("/delete/<num>",methods=["POST","GET"])
def delete_it(num):
        delete_rate= str(delete_moviue_by_primary(num))
        if delete_rate.lower()=="none":
            return "Deleted succesfully"
    
        return render_template("edit.html")

@app.route("/add",methods=["POST","GET"])

def add_it():
    form= MyForm()
    if form.validate_on_submit() or request.method=="POST":
        movie=form.movie.data
        

    return render_template("add.html",form=form)

if __name__ == '__main__':
    app.run(debug=True)
