class person:
    def __init__(self,name):
        self.name = name
        
    def show(self):
        print("I am a person")
        
class student(person):
    def __init__ (self,name):
        
        super().__init__(name)
    
    def show(self):
        super().show()
        
        print("And I am a student")
        
s1= student("Masum")

s1.show()