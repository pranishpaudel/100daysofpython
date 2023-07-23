def calculate(**kwargs):
    for (key,value) in kwargs.items():
        print(key)
        print(value)



calculate(add=5, mul=6)


class Car:

    def __init__(self, **pra):
        self.model= pra.get("model")
        self.name= pra.get("name")


car= Car(name="Range Rover", model="R-15")

print(car.model)