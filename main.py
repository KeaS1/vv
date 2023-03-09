class Car:
    def __init__(self, speed, name):
        self.speed = speed
        self.name = name
    def drive(self):
        print("Врум врум")
    def crash(self, Car):
        self.crash = Car
        Car.crash = self
    @property
    def speed1(self):
        return self.speed
class truck(Car):
    def drive(self):
        print("ветер в харю я хуярю")
audi = truck(80, "audi")
bmw = Car(120, "bmw")

audi.crash(bmw)
print(bmw.crash.name)
print(bmw.speed1)