
from flight_search import flightSearch
from data_manager import DataManager

ORIGIN_IASO= "LON"


class FlightData:

    def __init__(self):
        self.flight_obj= flightSearch()
        self.citywithpricelist= DataManager().get_min_prices()

        self.visitable_cities=[]

    def get_low_price(self):
        for pdata in self.citywithpricelist:
                appear_city= pdata["city"]
                appear_price= pdata["lowestPrice"]
                appear_IAST= pdata["iataCode"]
                actual_price= self.flight_obj.execute_search(ORIGIN_IASO,appear_IAST)
                if appear_price>actual_price:
                    wanttext= f"CITY: {appear_city}, Price: {actual_price}"
                    self.visitable_cities.append(wanttext)
        
        return self.visitable_cities









        

