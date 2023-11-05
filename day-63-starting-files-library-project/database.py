from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////Users/air/Desktop/100daysofpython/day-63-starting-files-library-project/new-books-collection.db"

# Create the extension
db = SQLAlchemy()
# Initialise the app with the extension
db.init_app(app)


##CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)




# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# # CREATE RECORD
# with app.app_context():
#     new_book = Book(id=2, title="Harry j", author="J. K. Rowling", rating=9.3)
#     db.session.add(new_book)
#     db.session.commit()




#READ THE DATABASE CONTENET
# with app.app_context():
#     result = db.session.execute(db.select(Book).where(Book.title == "Harry Potter"))
#     all_books = result.scalar()
#     print(all_books.rating)



#Update A Particular Record By Query

# with app.app_context():
#     book_to_update= db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
#     book_to_update.title= "NEW TITLE LOL"
#     db.session.commit()


#UPDATE A PARTCULAR RECORD BY PRIMARY KEY
# book_id = 1
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     # or book_to_update = db.get_or_404(Book, book_id)  
#     book_to_update.title = "Harry Potter and the Goblet of Fire"
#     db.session.commit() 

#    SHORTCUT TRICK TO GET A ELEMENT IN ONE LINE
# book_id = 2
# with app.app_context():
#     try:
#         book_to_update = db.get_or_404(Book, book_id)  
#         print(book_to_update.title)
#     except:
#         print("NOT FOUND")




#DELETE THE ELEMNET

# with app.app_context():
#     book_to_delete= db.get_or_404(Book,2)
#     db.session.delete(book_to_delete)
#     print(db.session.commit())
    

with app.app_context():
    all_books= Book.query.count()
    print(all_books)