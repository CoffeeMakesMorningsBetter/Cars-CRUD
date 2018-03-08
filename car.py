class Car():
    id = 1

    #class in singular
    #routes in plaural
    #database plaural
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.id = Car.id
        Car.id += 1