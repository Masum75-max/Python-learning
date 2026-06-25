class Grandfather:
    def land(self):
        print("dadar jomi ase")

class Father(Grandfather):
    def house(self):
        print("babar bari ase")

class Child(Father):
    def car(self):
        print("sontaner gari ase")

c = Child()
c.land()   # Grandfather থেকে এসেছে
c.house()  # Father থেকে এসেছে
c.car()    # নিজের মেথড