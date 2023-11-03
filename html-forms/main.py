from flask import Flask,render_template,request



app= Flask(__name__)


@app.route("/")
def index_home():
    return render_template("index.html")

@app.route("/login",methods=["POST"])
def return_something():
    if request.method == 'POST':
        fnamee= request.form["first"]
        password= request.form["password"]
        return render_template("giveinfo.html",f_name=fnamee,passs=password)



app.run(debug=True)