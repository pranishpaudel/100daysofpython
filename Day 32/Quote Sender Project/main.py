import smtplib
import datetime as dt
from random import randint

file= open("quotes.txt")

data= file.readlines()

def random_quote():
    quote= data[randint(0,102)]
    return quote

current_weekday= dt.datetime.now().weekday()

def send_quote():
    my_email= "mikey295t@gmail.com"
    password= "pdhhbunrhovjuslb"
    connection= smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr= my_email
                        , to_addrs= "topper7001@gmail.com",
                        msg=f"Subject:Quote\n\n{random_quote()}")
    connection.close()

if current_weekday==6:
    send_quote()
else:
    print("Wait till then boss!")