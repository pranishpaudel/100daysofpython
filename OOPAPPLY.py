class User:
  
  def __init__(self, user_id, username):
   self.id= user_id
   self.username= username
    



user1= User(111,"insa")
user2= User(432,"insa")

print(user1.id)
print(user2.id)
