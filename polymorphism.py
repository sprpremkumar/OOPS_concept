class car:
    def intro(self):
        print("Mode of Transport --> Road")
    def spec(self):
        print("Depends upon the car model")

class bmw(car):
    def spec(self):
        print("BMW 7 series --> 7.96 km/l")

class rollsroyce(car):
    def spec(self):
        print("Rolls Royce Phantom --> 9.8 km/l")

CAR=car()
BMW =bmw()
RR=rollsroyce()

BMW.intro()
CAR.spec()
RR.spec()