from replit import clear
#HINT: You can call clear() to clear the output in the console.
Bidders={}
Entry= True
while Entry==True:
  name= input("Enter your name")
  Bid= int(input("Enter $ of bid"))
  Bidders[name]=Bid
  que= input("Are there any other bider too?")
  if que=="N":
    Entry= False
    print("Giving output")
  else:
    Entry= True

#Compare highest bid
Bids=[]
for bid in Bidders:
  Bids.append(Bidders[bid])

print (Bids)

great= max(Bids)

for final in Bidders:
  if great== Bidders[final]: 
    print(f"The highest bidder is {final}")
  

print(Bidders)
    
  