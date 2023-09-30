from data_manager import DataManager
from check_flight import FlightData
from notification_manager import NotificationManager
from customer_acc import Acquire_Cust
import requests
from email import EMAIL


print("Welcome to Pranish Flight Club!")
print("We find best flight deals and send you")
nfirstt= input("What is your first name?")
nlastt= input("What is your last name?")

is_email_matched= False
while not is_email_matched:
    nemaill= input("What is your email?")
    nemailll= input("Please reconfirm your email?")
    if nemaill.lower()==nemailll.lower():
        is_email_matched=True
    else:
        userwant= input("Either Of the email not matched. Do you want to retry?(Y/N)")
        if userwant.lower()=="n":
            exit()
        else:
            is_email_matched=False


ac_cust= Acquire_Cust(nfirst= nfirstt,nlast=nlastt,nemail=nemaill).send_acquire()

print(ac_cust)

lowest_flight= FlightData().get_low_price()
print(lowest_flight)

for element in lowest_flight:
    city_info = element.split(', ')
    city = city_info[0].split(': ')[1]
    price = int(city_info[1].split(': ')[1])
    
    # Merge city and price in a single print statement
    msg_to_be_sent= f"City: {city}, Price: {price}"
    emaill= EMAIL(msg_to_be_sent
    # send_sms= NotificationManager().send_msg(msg_to_be_sent)














# data= DataManager().update_iasa()

# def search_flight(cityy):

#     fsearch= flightSearch().send_city_code(cityy)
#     return fsearch

# insa=2
# for pricee in data["prices"]:

#     if (pricee["iataCode"] ==""):

#         data_para= body = {
#           "price": {
#           "id" :insa,
#           "iataCode": search_flight(pricee["city"]) }}
        

#         data_url= requests.put(url=f"https://api.sheety.co/d0b1efc67d18564e79bd6d0ed95fa049/copyOfFlightDeals/prices/{insa}", json= data_para)






    
        
    

  
        






