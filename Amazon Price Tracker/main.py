import requests
from bs4 import BeautifulSoup
import smtplib


AMAZON_ENDPOINT= "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

TARGET_PRICE= 100

def send_email(email,email_text):
        my_email= "sheikhalhabib9@gmail.com"
        password= "qhhs cbxn wqvj mrfy"
        connection= smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email,password=password)
        kemu= connection.sendmail(from_addr= my_email
                            , to_addrs= email,
                            msg=email_text)
        connection.close()


header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

AMAZON_DATA = requests.get(AMAZON_ENDPOINT, headers=header).text

soup= BeautifulSoup(AMAZON_DATA,"html.parser")

amazon_price= soup.find(name="span", class_="a-offscreen").getText()[1:]
print(amazon_price)


if float(amazon_price)<float(TARGET_PRICE):
        email_text=f"The current price in amazon is {amazon_price} which is less than {TARGET_PRICE}"
        insa= send_email("pranishisop@gmail.com",email_text)







