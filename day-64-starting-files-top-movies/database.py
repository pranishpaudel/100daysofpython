from flask_sqlalchemy import SQLAlchemy


class DataBase:



    def __init__(self,flaskapp):
        self.flaskapp=flaskapp
        self.flaskapp.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////Users/air/Desktop/100daysofpython/day-64-starting-files-top-movies/databasenew.db"
        self.db= SQLAlchemy()
        self.db.init_app(flaskapp)

        class Movie(self.db.Model):
            id = self.db.Column(self.db.Integer, primary_key=True)
            title =  self.db.Column(self.db.String(250), unique=True, nullable=False)
            year =  self.db.Column(self.db.String(250), nullable=False)
            description =  self.db.Column(self.db.String(250), nullable=False)
            rating =  self.db.Column(self.db.Float, nullable=False)
            ranking =  self.db.Column(self.db.Integer, nullable=False)
            review= self.db.Column(self.db.String(250), nullable=False)
            img_url= self.db.Column(self.db.String(250), nullable=False)


    
    def create_database(self):
        with self.flaskapp.app_context():
            self.db.create_all()


    def create_new_record(self):
        with self.flaskapp.app_context():
            new_movie = Movie(
                title="Phone Booth",
                year="2002",  # You should use a string for the year
                description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
                rating=7.3,
                ranking=10,
                review="My favorite character was the caller.",
                img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
            )
            self.db.session.add(new_movie)
            self.db.session.commit()