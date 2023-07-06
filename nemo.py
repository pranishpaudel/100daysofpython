class Animal:

 def __init__(self):
   self.num_eyes= 2

 def breathe(self):
   print("Lungs, gills")

class Fish(Animal):

  def __init__(self):
    super().__init__()

  def breathe(self):
    super().breathe()
    print("Doing this inside the fucking water")

  def go(self):
    print("FISHES CAN BREATHE THROUGH THE LUNGS")


nemo= Fish()
nemo.breathe()
print(nemo.num_eyes)