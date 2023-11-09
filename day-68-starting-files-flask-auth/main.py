from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'F#d#E@$43FDFDFD'

# CONNECT TO DBCD#3
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/air/Desktop/100daysofpython/day-68-starting-files-flask-auth/instance/users.db'
db = SQLAlchemy()
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


CHEAT_FILE_PATH= "day-68-starting-files-flask-auth/static/files"
# CREATE TABLE IN DB
class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
 
 
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register',methods=["POST","GET"])
def register():
    if request.method=="POST":
        email= request.form["email"]
        password= request.form["password"]
        hash= generate_password_hash(password,method='pbkdf2', salt_length=10)
        name= request.form["name"]
        with app.app_context():
                new_user= User(email=email,
                            password=hash,
                            name=name)
                db.session.add(new_user)
                insa= db.session.commit()
                print(new_user.get_id())
                login_user(new_user)
                return redirect(f"secrets/{name}")

    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login',methods=["POST","GET"])
def login():
    if request.method=="POST":
        email= request.form["email"]
        password= request.form["password"]
        try:
            result = db.session.execute(db.select(User).where(User.email == email))
            user = result.scalar()
            if check_password_hash(user.password, password):
                flash('You were successfully logged in')
                login_user(user)
                return redirect(url_for('secrets',name=user.name))
        except:
            error= "EMAIL OR PASSWORD WAS INCORRECT"
            return render_template('login.html', error=error)

    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets/<name>',methods=["POST","GET"])
@login_required
def secrets(name):
    return render_template("secrets.html",name=name, logged_in=current_user.is_authenticated)


@app.route('/logout')

def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)





