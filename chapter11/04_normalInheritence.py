class animal:
    def __init__(self,name):
        self.name=name
        
    def eat(self):
        print(f"{self.name} is eating")
        
class dog(animal):
    
    def makeSound(self):
        print(f"{self.name} is doing gheu gheu")
        
d=dog("tommy")

d.eat()
d.makeSound()