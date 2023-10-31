import requests
import time


URL__ENDPOINT= "https://api.nopecha.com/token/"



req_json= {
    'key': 'sub_1O6274CRwBwvt6pteIGa8SUd',
    'type': 'recaptcha2',
    'sitekey': '6Ld_8U8UAAAAAHjwp-RbI3haQic6UfH2Zo4lVa40',
    'url': 'https://www.msisurfaces.com/shoppingcart.aspx'
}
send_req= requests.post(url=URL__ENDPOINT,json=req_json).json()["data"]
print(send_req)




#get token requests

para={
    'key': 'sub_1O6274CRwBwvt6pteIGa8SUd',
    'id': send_req
}
time.sleep(10)

get_req= requests.get(url=URL__ENDPOINT,params=para).json()
print(get_req)