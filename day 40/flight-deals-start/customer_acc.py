import requests
cusacquire_ENDPOINT= "https://api.sheety.co/d0b1efc67d18564e79bd6d0ed95fa049/customerAcquisation/sheet1"


class Acquire_Cust:

    def __init__(self,nfirst,nlast,nemail):
        self.nemail= nemail
        self.nfirst= nfirst
        self.nlast= nlast
        self.cusparams={
            "sheet1":{
            "firstname": self.nfirst,
            "lastname": self.nlast,
            "email": self.nemail,
        }}
    

    def send_acquire(self):
        self.header= {
            "Content-Type": "application/json",
        }
        self.cusreq= requests.post(url= cusacquire_ENDPOINT, json= self.cusparams,headers=self.header).json()
        return self.cusreq