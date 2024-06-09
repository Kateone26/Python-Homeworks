class car:
    wheel = 4
    steering_Wheel = 1
    engine = 1
    gas_pedal = 1

    def __init__(self, seats, fit, isEco = True):
        self.seats = seats
        self.fit = fit
        if isEco == False:
            self.isEco = "is not eco friendly"
        else:
            self.isEco = "is eco friendly"

    def carIntroduction(self):
        print(f"Hi my car has {self.seats} seats, it can fit {self.fit} person and it {self.isEco}")

    @staticmethod
    def person_Per_Family(*numbers):
        return f"We're looking for a car that will fit {sum(numbers)} passengers"

    @classmethod
    def wheel_number(cls):
        print(f"My car only has {cls.wheel} wheels")

    @classmethod
    def gasPedanNumber(cls, breaks, teaching = False):
        if teaching == False:
            print(f"My car only has {cls.gas_pedal} gas pedal and {breaks} break pedal as it isn't a teaching car ")
        else:
            print(f"My car only has {cls.gas_pedal} gas pedal and {breaks} break pedal as it is a teaching car ")

    def __repr__(self):
        return f"(Seat number: {self.seats}, Fits {self.fit} person, is eco: {self.isEco})"

car1 = car(4,5, False)
car2 = car(7, 8, True)
car3 = car(22,23,False)
car4 = car(44,50,True)
car5 = car(18,20,True)

car4.wheel = 8
car5.wheel = 6

print(car.person_Per_Family(5,4,9))
car.wheel_number()
car1.carIntroduction()
car.gasPedanNumber(1, False)
print(car1, car2)

print(car4.wheel)
print(car5.wheel)