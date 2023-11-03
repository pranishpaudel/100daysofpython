from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField
from wtforms.validators import DataRequired
import csv


CURRENT_CSV= "day-62-starting-files-coffee-and-wifi/cafe-data.csv"
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
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap= Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    cafe_location = StringField('Cafe Location on Google Maps', validators=[DataRequired()])
    cafe_opening = StringField('Cafe Opening time in Morning', validators=[DataRequired()])
    cafe_ending = StringField('Cafe Ending time in Evening', validators=[DataRequired()])
    cafe_coffee = SelectField('Coffee Rating', validators=[DataRequired()],
                             choices=[('☕'), ('☕☕'), ('☕☕☕'), ( '☕☕☕☕'), ('☕☕☕☕☕')])
    wifi_rating = SelectField('Wifi Rating', validators=[DataRequired()],choices=[('💪'), ('💪💪'), ('💪💪💪'), ( '💪💪💪💪'), ('💪💪💪💪💪')])
    power_rating = SelectField('Power socket availability', validators=[DataRequired()],choices=[('	🔌'), ('🔌🔌'), ('🔌🔌🔌'), ( '🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌')])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=["POST","GET"])
def add_cafe():
    form = CafeForm()
    if not form.validate_on_submit():
        return render_template('add.html', form=form)
    else:
        cafe_name= form.cafe.data
        Location= form.cafe_location.data
        Open= form.cafe_opening.data
        Close= form.cafe_ending.data
        Coffee= form.cafe_coffee.data
        Wifi= form.wifi_rating.data
        Power= form.power_rating.data
        new_row = [cafe_name,Location,Open,Close,Coffee,Wifi,Power]

        with open(CURRENT_CSV, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            # Write the new row to the CSV file
            writer.writerow(new_row)
        return render_template("cafes.html")

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()



@app.route('/cafes')
def cafes():
    with open('day-62-starting-files-coffee-and-wifi/cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
