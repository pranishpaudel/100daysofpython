import requests



class Blog:

    def __init__(self):
         self.blog_url= requests.get("https://api.npoint.io/126573c3358ffdf5c119").json()


    

    def return_all_info(self):
         return self.blog_url
    


    def return_specific(self,r_num):
         return self.blog_url[r_num]