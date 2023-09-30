import smtplib
class EMAIL:

    def __init__(self,email):

        self.email= email
        my_email= "mikey295t@gmail.com"
        password= "pdhhbunrhovjuslb"
        connection= smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr= my_email
                            , to_addrs= self.email,
                            msg=f"Subject:Birthday Wish")
        connection.close()

