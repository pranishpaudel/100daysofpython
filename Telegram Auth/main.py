from flask import Flask, render_template, request, redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required,logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from telegram import Bot, ParseMode
import requests
from random import randint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'CInXASS$$$GGFDFSD'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/air/Desktop/100daysofpython/Telegram Auth/instance/tg_user.db'
db = SQLAlchemy(app)

bot = Bot(token="6730263119:AAHqefeyacHdDADiDbryx3F9gC5H5egeNxY")

def generate_otp():
    return str(randint(100000, 999999))

def is_all_digits(text):
    return text.isdigit()

login_manager = LoginManager()
login_manager.init_app(app)

# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    telegram_userid = db.Column(db.String(100), unique=True)
    telegram_username = db.Column(db.String(100), unique=True)
    profile_name = db.Column(db.String(100))
    authorized_ip = db.Column(db.String(100))
    sign_up_otp = db.Column(db.String(100))
 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        profile_name = request.form["profile_name"]
        telegram_username = request.form["telegram_username"]
        telegram_useridd = request.form["telegram_userid"]

        if not is_all_digits(telegram_useridd):
            return "TELEGRAM USERID IS INVALID"

        user = User.query.filter_by(telegram_userid=telegram_useridd).first()

        if not user:
            ip_address = requests.get("https://api.animaker.com/upload/ip/").json()["ip"]
            current_user_otp = generate_otp()
            message_text = (
                f"*Hey {profile_name}!*\n"
                f"Welcome to iTsFrosTyZ Checker\n"
                f"*Your otp for sign up is:* `{current_user_otp}`\n"
                f"*Userid:* `{telegram_useridd}`\n"
                f"*Current IP AUTHORIZED:* `{ip_address}`"
            )
            try:
                bot.send_message(chat_id=telegram_useridd, text=message_text, parse_mode=ParseMode.MARKDOWN)
                new_user = User(
                    telegram_userid=str(telegram_useridd),
                    telegram_username=str(telegram_username),
                    profile_name=str(profile_name),
                    authorized_ip=str(ip_address),
                    sign_up_otp=str(current_user_otp)
                )
                db.session.add(new_user)
                db.session.commit()
        
                return redirect(url_for('register_otp', user_id=new_user.id,log_type="Sign Up"))
            except:
                return "THERE WAS SOME PROBLEM WHILE SENDING OTP"
        else:
            return "USER ALREADY REGISTERED"
    
    return render_template("register.html")

@app.route("/otp/<user_id>/<log_type>", methods=["POST", "GET"])
def register_otp(user_id,log_type):
    if log_type=="Sign Up":
        user = User.query.get(user_id)
    else:
        user= User.query.filter_by(telegram_userid=user_id).first()

    if request.method == "POST":
        user_input_otp = request.form["user_otp"]

        if user and user_input_otp == user.sign_up_otp:
            now_ip = requests.get("https://api.animaker.com/upload/ip/").json()["ip"]
            if str(now_ip)==user.authorized_ip:
                login_user(user)
                return redirect(url_for('secrets'))
            else:
                if user and log_type=="Sign Up":
                    db.session.delete(user)
                    db.session.commit()
                return "<h1><b>The ip address is not recorded ip address in database</b></h1>"
        else:
            if user and log_type=="Sign Up":
                db.session.delete(user)
                db.session.commit()
            return "<h1><b>THE OTP DOES NOT MATCH</b></h1>"
    
        

    return render_template("input_otp.html",log_type=log_type)



@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user_id = request.form['tg_userid']
        with app.app_context():

            user = User.query.filter_by(telegram_userid=user_id).first()
            if user:
                ip_address = requests.get("https://api.animaker.com/upload/ip/").json()["ip"]
                current_user_otp = generate_otp()
                otp_user= User.query.get_or_404(user.id)
                otp_user.sign_up_otp=current_user_otp
                db.session.commit()
                message_text = (
                    f"*Hey {user.profile_name}!*\n"
                    f"*Your otp for login is:* `{current_user_otp}`\n"
                    f"*Userid:* `{user_id}`\n"
                    f"*Current IP AUTHORIZED:* `{user.authorized_ip}`"
                )
            
                bot.send_message(chat_id=user_id, text=message_text, parse_mode=ParseMode.MARKDOWN)
                return redirect(url_for('register_otp', user_id=user_id,log_type="Login"))

            else:
                return redirect(url_for('register'))
     

    return render_template("/login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/download')
@login_required
def download():
    # Your download logic goes here for authenticated users
    pass

if __name__ == "__main__":
    app.run(debug=True)
