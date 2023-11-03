from flask import Flask
from flask import render_template,request
from blog import Blog
import smtplib


def send_message(input_message):
 

    my_email= "pkpoudelpranishma@gmail.com"
    password= "fwjhoovxfrvzzods"
    connection= smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email,password=password)
    insa= connection.sendmail(from_addr= my_email
                        , to_addrs= "pranishisop@gmail.com",
                        msg=f"Subject:Website Form info\n\n{input_message}")
    connection.close()
    return insa



app = Flask(__name__)


blog= Blog()
@app.route('/')
def hello_world():
    return render_template("index.html",data=blog.return_all_info())


@app.route("/about.html")
def about_info():
    return render_template("about.html")

@app.route("/contact.html")
def contact_info():
    return render_template("contact.html")

@app.route("/post.html")
def post_info():
    return render_template("post.html")


@app.route("/postinfo.html/<num>")
def info_post(num):
    send_info= blog.return_specific(int(num))
    return render_template("post_info.html",info=send_info)


@app.route("/submit",methods=["POST"])
def return_info():
    full_name= request.form["message"]
    email= request.form["email"]
    phone= request.form["phone"]
    message= request.form["message"]
    msg_to_send= f"Full name: {full_name}\n Email: {email} \n Phone Number: {phone} \n Message: {message}"
    vinda=send_message(msg_to_send)
    if "{}" in str(vinda):
        return "Form submitted succesfully"
    else:
        return f"There has been some errors: Error code: {vinda}"
    
    

app.run(debug=True)