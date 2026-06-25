class student:
    
    def __init__(self,name,roll,section):
        self.name=name
        self.roll=roll
        self.section=section
        
        
    def show(self):
        print("My name is ",self.name," My roll is :",self.roll)
        



s1= student("masum",102,'b')
s2=student("tashfe",102,'b')

s1.show()

s2.show()