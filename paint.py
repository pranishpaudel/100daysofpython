
import math

def paint_calc(height,width,cover):
  numc= (height*width)/cover
  num= math.ceil(numc)
  print(f"The required number of cans is {num}")
  
# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)




