from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////Users/air/Desktop/100daysofpython/day-63-starting-files-library-project/new-books-collection.db"

# Create the extension
db = SQLAlchemy()
# Initialise the app with the extension
db.init_app(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


# with app.app_context():
#     db.create_all()

def get_all_books():
    with app.app_context():
        all_books_now= Book.query.all()
        return all_books_now
    
def get_books_count():
    with app.app_context():
        book_count= Book.query.count()
        return book_count



def get_book_by_primary(num,newrate):
    with app.app_context():
        book_name= db.get_or_404(Book,num)
        book_name.rating=newrate
        done= db.session.commit()
        print( done)

def get_book_info_primary(num):
    with app.app_context():
        book_name= db.get_or_404(Book,num)
        total_books= []
        total_books.append(book_name.title)
        total_books.append(book_name.rating)
        return total_books



@app.route('/')
def home():
    return render_template("index.html",listcount=get_books_count(),book_list=get_all_books())


@app.route("/added", methods=["POST","GET"])
def added():
    if request.method == "POST":
        Title = request.form["booktitle"]
        Author= request.form["bookauthor"]
        Rating= float(request.form["bookrating"])
        if (type(Rating)==float or type(Rating)==int):
            with app.app_context():
                new_book= Book(title=Title, author=Author, rating=Rating)
                db.session.add(new_book)
                db.session.commit()
 

            return render_template("add.html")
        else:
            return "SOME ERROR IN DATABASE"
    return "This is not a POST request."

@app.route("/add", methods=["GET"])
def add():
    return render_template("add.html")


@app.route("/newrate/<num>",
 methods=["GET","POST"])
def new_rating(num):
      if request.method=="POST":
        rating= float(request.form["ratenew"])
        try :
            get_book_by_primary(num,rating)
            return render_template("index.html")
        except:
            return "SOME ERRORS"

    # return get_book_by_primary(num,rating)
      return render_template("editrate.html",total_books=get_book_info_primary(int(num)))


if __name__ == "__main__":
    app.run(debug=True)

