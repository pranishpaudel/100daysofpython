import random
num= random.randint(1,100)
#print(num)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

user_choice= input("What level do you wanna play in? EASY OR HARD")

def chosen_num(usernum):
  if usernum==num:
    return 0
def compare_num(usernum):
  if usernum<num:
    print("TOO LOW")
  else:
    print("TOO HIGH")


def userlev(lev):
  c=0
  is_finished=False
  while is_finished==False:
    usernum= int(input("Enter your number"))
    c+=1
    if c==lev:
      is_finished=True
      print("You have ran out of tries")
    elif usernum!=num:
      compare_num(usernum)
    
    elif chosen_num(usernum)==0:
      print(f"Your guess was right! and the number was {num}")
      is_finished=True
      
if user_choice.lower()=="easy":
  userlev(5)
else:
  userlev(10)

    
  
  


