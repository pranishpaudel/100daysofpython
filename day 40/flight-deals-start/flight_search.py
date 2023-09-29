import requests
from datetime import datetime, timedelta

FLIGHT_SEARCH_ENDPOINT= "https://api.tequila.kiwi.com"
F_API_KEY= "fmIG7NcqgB_dkJyCqlVZ8a32rP-I-IIe"


class flightSearch():
    
    def __init__(self):

        self.fheader={
              "apikey": F_API_KEY,
              "accept": "application/json",
        }
      

    def send_city_code(self,city):
        
        self.citycode= requests.get(url= f"{FLIGHT_SEARCH_ENDPOINT}/locations/query?term={city}&locale=en-US&location_types=city&active_only=true",headers=self.fheader).json()
        return self.citycode["locations"][0]["code"]
    


    def search_flight(self,origin_city_code, destination_city_code ):

        self.current_date = datetime.now()

 
        self.six_months_later = self.current_date + timedelta(days=6*30)


        self.current_date_formatted = self.current_date.strftime('%d/%m/%Y')
        self.six_months_later_formatted = self.six_months_later.strftime('%d/%m/%Y')

        self.headers = {"apikey": F_API_KEY,
                        "accept" : "application/json",}
        self.query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from":  "30/09/2023",
            "date_to": self.six_months_later_formatted,
            "curr": "GBP"
        }

        self.searchf= requests.get(url="https://api.tequila.kiwi.com/v2/search",headers=self.headers,params= self.query).json()
        return (self.searchf) 
    
    def execute_search(self,city1,city2):

          flightsearch= self.search_flight(city1,city2)

          flightprice= flightsearch["data"][0]["price"]
          
          return flightprice




