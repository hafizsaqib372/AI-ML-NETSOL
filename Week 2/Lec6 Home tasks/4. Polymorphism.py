class Vehicle:
    def move(self):
        print("Vehicle is moving")


class Car(Vehicle):
    def move(self):
        print("Car is driving")


class Plane(Vehicle):
    def move(self):
        print("Plane is flying")


vehicles = [Car(), Plane()]

for v in vehicles:
    v.move()
