import requests

class Post:
    def __init__(self):
        self.blog_urll= "https://api.npoint.io/126573c3358ffdf5c119"
        self.response= requests.get(self.blog_urll).json()
        
        
    def send_all_post(self):
       self.all_posts= self.response
       return self.all_posts
    
    def send_wanted_post(self,numm):
        return self.response[numm]
