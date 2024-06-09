class Car:
    wheel = 4
    steering_Wheel = 1
    engine = 1
    gas_pedal = 1

    def __init__(self, seats, fit, iseco=True):
        self.seats = seats
        self.fit = fit
        if iseco:
            self.iseco = "is eco friendly"
        else:
            self.iseco = "is not eco friendly"

    def car_introduction(self):
        print(f"Hi my car has {self.seats} seats, it can fit {self.fit} person and it {self.iseco}")

    @staticmethod
    def person_per_family(*numbers):
        return f"We're looking for a car that will fit {sum(numbers)} passengers"

    @classmethod
    def wheel_number(cls):
        print(f"My car only has {cls.wheel} wheels")

    @classmethod
    def gas_pedal_number(cls, breaks, teaching=False):
        if not teaching:
            print(f"My car only has {cls.gas_pedal} gas pedal and {breaks} break pedal as it isn't a teaching car ")
        else:
            print(f"My car only has {cls.gas_pedal} gas pedal and {breaks} break pedal as it is a teaching car ")

    def __repr__(self):
        return f"(Seat number: {self.seats}, Fits {self.fit} person, is eco: {self.iseco})"


car1 = Car(4, 5, False)
car2 = Car(7, 8, True)
car3 = Car(22, 23, False)
car4 = Car(44, 50, True)
car5 = Car(18, 20, True)

car4.wheel = 8
car5.wheel = 6

print(Car.person_per_family(5, 4, 9))
Car.wheel_number()
car1.car_introduction()
Car.gas_pedal_number(2, True)
print(car1, car2)

print(car4.wheel)
print(car5.wheel)
