height= int(input("Enter your height"))
weight= int(input("Enter your weight"))

bmi= weight / height **2

if height >3:
    raise ValueError("You aren't godzilla lol3")
print(bmi)