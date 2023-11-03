from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from form import MyForm
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap5



ADMIN_EMAIL= "admin@email.com"
ADMIN_PASSWORD= '12345678'

app = Flask(__name__)
app.secret_key = 'fs4ndase32easdsadassdf'

csrf = CSRFProtect(app)

bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    form= MyForm()
    return render_template("form.html",form=form)

@app.route("/login",methods=["POST"])
def login_info():
    form= MyForm()
    if form.validate_on_submit and request.method=="POST":
        email=form.email.data
        password= form.password.data
        if email==ADMIN_EMAIL and ADMIN_PASSWORD==password:
            return render_template("success.html")
        else:
           return render_template("denied.html")




    


if __name__ == '__main__':
    app.run(debug=True)
