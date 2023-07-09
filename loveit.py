# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
namek= name1 + name2
name= namek.upper()
sc1= name.count("T")
sc2= sc1+ name.count("R")
sc3= sc2+ name.count("U")
sc= sc3+ name.count("E")

sci= name.count("L")
scii= sci+ name.count("O")
sciii= scii+ name.count("V")
sc1= sciii+ name.count("E")

score= str(sc)+str(sc1)
sint= int(score)
if (sint<10) or (sint >90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (sint>40) and (sint<50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")






