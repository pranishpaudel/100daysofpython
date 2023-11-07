from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

MOVIE_ENDPOINT= "https://api.themoviedb.org/3/search/movie"
HEADER = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyY2U0MWI1Y2Y2ZDczZDg5OWI4YWYxNjFlOWE1ZDdmNyIsInN1YiI6IjY1NDhmYzJmNmJlYWVhMDE0YjY5MWRhOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.g69PyrrWoyfKtloqxDSpYBXiPYeVcJqL0tgN6V2ovQ8"
}



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



def return_all_records():
    with app.app_context():
        all_movies= Movie.query.all()
        return all_movies


def search_movie_by_name(wanted_movie):


    movie_data= requests.get(url=f"{MOVIE_ENDPOINT}?query={wanted_movie}&include_adult=false&language=en-US&page=1",headers=HEADER).json()["results"]
    return (movie_data)




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
        sort_movies_in_order()
        done= db.session.commit()
        return done


def sort_movies_in_order():
    with app.app_context():
        result = db.session.execute(db.select(Movie).order_by(Movie.rating))
        all_movies = result.scalars().all() # convert ScalarResult to Python List

        for i in range(len(all_movies)):
            all_movies[i].ranking = len(all_movies) - i
        db.session.commit()


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
        movie_data= search_movie_by_name(movie)
        print(movie_data)
        return render_template("select.html",current_list=movie_data)


    return render_template("add.html",form=form)

@app.route("/confirm_add/<movie_name>/<movie_release>/<movie_image>/<movie_description>",methods=["GET","POST"])

def confirm_add(movie_name,movie_release,movie_image,movie_description):

    with app.app_context():

        new_movie = Movie(
        title=movie_name,
        year=movie_release,
        description=movie_description,
        rating=0,
        ranking=9,
        review="Review not set yet",
        img_url=f"https://image.tmdb.org/t/p/w500/{movie_image}"
        )

        db.session.add(new_movie)
        insa= db.session.commit()
        result = db.session.execute(db.select(Movie).where(Movie.title == movie_name))
        all_movies = result.scalar()
        sort_movies_in_order()
        if str(insa).lower()=="none":
            return redirect(url_for('edit_it',insa=all_movies.id))



    


if __name__ == '__main__':
    app.run(debug=True)
