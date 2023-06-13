from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_taking= True
Menu = Menu()
CoffeeMaker= CoffeeMaker()
MoneyMachine= MoneyMachine()
print(Menu.get_items())
while is_taking:
  userchoice= input("Enter the drink you want")
  if userchoice=="report":
    print(CoffeeMaker.report())
    print(MoneyMachine.report())
  elif userchoice=="off":
    is_taking=False
  else:
    drink= Menu.find_drink(userchoice)
    print(drink)
    if CoffeeMaker.is_resource_sufficient(drink)==True and MoneyMachine.make_payment(drink.cost):
       CoffeeMaker.make_coffee(drink)

      
    
      
    
   
                
  


