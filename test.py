class Car():

    def __init__(self,type,year):

        self.vehicle = "car"
        self.type = type
        self.year = year

    def printModel(self):
        print(f"The {self.vehicle} model is {self.type} The year is {self.year}")

bmw = Car("bmw",2000)
bmw.printModel()
