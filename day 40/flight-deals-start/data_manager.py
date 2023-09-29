import requests
from flight_search import flightSearch

SHEET_ENDPOINT= "https://api.sheety.co/d0b1efc67d18564e79bd6d0ed95fa049/copyOfFlightDeals/prices"

class DataManager:
    
    def __init__(self):
        self.sheet_get= requests.get(SHEET_ENDPOINT).json()
        self.count=1
           
    
    def return_data(self):
        return self.sheet_get
    
    
    def update_iasa(self):
        
     for self.pricee in self.sheet_get["prices"]:

        if (self.pricee["iataCode"] ==""):

            self.fsearch= flightSearch()

            self.data_para = {
            "price": {
            "id" :self.count,
            "iataCode": self.fsearch.send_city_code(self.pricee["city"])}}
            
            self.count+=1
            

            self.data_url= requests.put(url=f"https://api.sheety.co/d0b1efc67d18564e79bd6d0ed95fa049/copyOfFlightDeals/prices/{self.count}", json= self.data_para).json()


    def get_min_prices(self):
           self.city_lowest_price_list = [{'city': item['city'], 'lowestPrice': item['lowestPrice'], 'iataCode': item['iataCode']} for item in self.sheet_get['prices']]
           return self.city_lowest_price_list

        
        
