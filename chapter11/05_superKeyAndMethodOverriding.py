class engineer:
    def __init__(self,name,id):
        self.name = name
        self.id=id
    def salary(self):
        
        print("Shadharon kormocharir beton")
        
class softwareEngineer(engineer):
    
    def __init__(self,name,id,language):
        
        super().__init__(name,id)
        self.language=language
        
    def show(self):
        print(f"My name is {self.name} my id no is {self.id} and my language is {self.language}")
        
    def salary(self):        # method overriding
        print("this is the salary of a soowtware engineer")  
        

eng = softwareEngineer("masum",102,"py")

eng.salary() 
    