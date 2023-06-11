import menu

def sendreport():
  print(menu.resources)
  rwater= menu.resources["water"]
  rmilk= menu.resources["milk"]
  rcoffee= menu.resources["coffee"]
  return rwater, rmilk, rcoffee


def checkingredient(coffeename):
  minimumwater = menu.MENU[coffeename]["ingredients"]["water"]
  if coffeename!="espresso":
    minimummilk= menu.MENU[coffeename]["ingredients"]["milk"] 
  else:
    minimummilk=0
  minimumcoffee= menu.MENU[coffeename]["ingredients"]["coffee"] 
  reqwater = menu.resources["water"]
  
  reqmilk = menu.resources["milk"]
  
  reqcoffee = menu.resources["coffee"] 

  totalcost=0

  if (reqwater>=minimumwater) and (reqmilk>=minimummilk) and (reqcoffee>=minimumcoffee):
    totalcost= menu.MENU[coffeename]["cost"]
    return totalcost
  else:
    return 0


def updateresource(userchoice):
    minimumwater = menu.MENU[userchoice]["ingredients"]["water"]
    if userchoice != "espresso":
        minimummilk = menu.MENU[userchoice]["ingredients"]["milk"]
    else:
        minimummilk = 0
    minimumcoffee = menu.MENU[userchoice]["ingredients"]["coffee"]
    menu.resources["water"] -= minimumwater
    menu.resources["milk"] -= minimummilk
    menu.resources["coffee"] -= minimumcoffee

  

def usercoin():
  uquaters= int(input("how many quarters?:"))
  udimes= int(input("how many dimes?:"))
  unickles= int(input("how many nickles?:"))
  upennies= int(input("how many pennies?:"))
  usum= (uquaters*0.25)+(udimes*0.10)+(unickles*0.05)+(upennies*0.01)
  return usum

def comparecoin(userchoice):
  userrcoin=usercoin()
  reqcoin= checkingredient(userchoice)
  if userrcoin>=reqcoin:
    leftcoin=0
    leftcoin= userrcoin - reqcoin
    print(f"Here is your ${leftcoin} in charge")
    updateresource(userchoice)

  else:
    print("Sorry there is not enough coin")
  
  
is_finished=False

while is_finished==False:                            
    userchoice= input("What would you like? (espresso/latte/cappuccino):").lower()

    if (checkingredient(userchoice))!=0:
       if userchoice=="report":
         sendreport()
       elif userchoice=="cappuccino":
         print(checkingredient("cappuccino"))
         comparecoin(userchoice)
       elif userchoice=="latte":
         print(checkingredient("latte"))
         comparecoin(userchoice)
       elif userchoice=="espresso":
         print(checkingredient("espresso"))
         comparecoin(userchoice)
    else:
      is_finished==True
      print("You dont have enough resources")


    
    



  