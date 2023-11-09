from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from random import randint
from telegram import Bot,ParseMode
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'CInXASS$$$GGFDFSD'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/air/Desktop/100daysofpython/Telegram Auth/instance/tg_user.db'
db = SQLAlchemy()
db.init_app(app)

bot = Bot(token="6730263119:AAHqefeyacHdDADiDbryx3F9gC5H5egeNxY")

def generate_otp():
    return str(randint(100000, 999999))

def is_all_digits(text):
    return text.isdigit()

login_manager = LoginManager()
login_manager.init_app(app)

# Create a user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return User.query.get_or_404(user_id)


# CREATE TABLE IN DB
class User(UserMixin,db.Model):
    id = db.Column(db.Integer, unique=True)
    telegram_userid = db.Column(db.String(100), primary_key=True)
    telegram_username = db.Column(db.String(100), unique=True)
    profile_name = db.Column(db.String(100))
    authorized_ip = db.Column(db.String(100))
    sign_up_otp = db.Column(db.String(100))
 
 
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register',methods=["POST","GET"])
def register():
    if request.method=="POST":
        with app.app_context():
            profile_name= request.form["profile_name"]
            telegram_username= request.form["telegram_username"]
            telegram_useridd= (request.form["telegram_userid"])
            if not is_all_digits(telegram_useridd):
                return "TELEGRAM USERID IS IN-VALID"
            result = db.session.execute(db.select(User).where(User.telegram_userid == telegram_useridd))
            user = result.scalar()
            if not user:
                ip_address= requests.get("https://api.animaker.com/upload/ip/").json()["ip"]
                current_user_otp= generate_otp()
                message_text = (
            f"*Hey {profile_name}!*\n"
            f"Welcome to iTsFrosTyZ Checker\n"
            f"*Your otp for sign up is:* `{current_user_otp}`\n"
            f"*Userid:* `{telegram_useridd}`\n"
            f"*Current IP AUTHORIZED:* `{ip_address}`"
        )       
                try:
                    bot.send_message(chat_id=telegram_useridd, text=message_text, parse_mode=ParseMode.MARKDOWN)
                    new_user = User(telegram_userid=str(telegram_useridd),
                                    telegram_username=str(telegram_username),
                                    profile_name=str(profile_name),
                                    authorized_ip=str(ip_address),
                                    sign_up_otp=str(current_user_otp))
                    db.session.add(new_user)
                    db.session.commit()       
        
                    return redirect(url_for('register_otp',user_id=telegram_useridd))
                except:
                    return "THERE WAS SOME PROBLEM WHILE SENDING OTP"
        
            else:
                return "USER ALREADY REGISTERED"
    
    
    
    return render_template("register.html")


@app.route("/otp/<user_id>",methods=["POST","GET"])
def register_otp(user_id):
    if request.method=="POST":
        with app.app_context():
            user_input_otp= request.form["user_otp"]
            real_sign_otp= User.query.get_or_404(user_id)
            if user_input_otp==real_sign_otp.sign_up_otp:
                return redirect(url_for('secrets'))
            else:
                db.session.delete(real_sign_otp)
                db.session.commit()
                return "NOT AUTHORIZED"
                

    return render_template("input_otp.html")


@app.route('/login')
def login():
    return render_template("login.html")

@login_required
@app.route('/secrets')
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    pass


if __name__ == "__main__":
    app.run(debug=True)
