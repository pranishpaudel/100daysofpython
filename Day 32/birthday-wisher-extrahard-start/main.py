##################### Extra Hard Starting Project ######################
import random
import pandas
import datetime as dt
import smtplib

choicee=[0,1]

def send_wish():
 
    letter,send_email=main_thing()

    my_email= "mikey295t@gmail.com"
    password= "pdhhbunrhovjuslb"
    connection= smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr= my_email
                        , to_addrs= send_email,
                        msg=f"Subject:Birthday Wish\n\n{letter}")
    connection.close()

# 2. Check if today matches a birthday in the birthdays.csv
def main_thing():

    with open("Day 32/birthday-wisher-extrahard-start/birthdays.csv") as file:
        data= (pandas.read_csv(file))
        send_email= data["email"][random.choice(choicee)]
        send_month= data["month"][random.choice(choicee)]
        send_day= data["day"][random.choice(choicee)]
        send_name= data["name"][random.choice(choicee)]
        if dt.datetime.now().month==send_month and dt.datetime.now().day==send_day:

            file_number = random.randint(1, 3)
            file = open(f"Day 32/birthday-wisher-extrahard-start/letter_templates/letter_{file_number}.txt")
            data= file.read()
            letter = data.replace("[NAME]",send_name)
            return letter,send_email

        
send_wish()

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




