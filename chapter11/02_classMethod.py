class student:
    school_name="ABC SCHOOOL"
    
    def __init__(self,name):
        self.name = name
        
    @classmethod
    def school_name_change(cls,name):
        cls.school_name=name
        
    def show(self):
        
        print(self.name, self.school_name)
        

s1= student("Masum")

s1.show()

s1.school_name_change("DBC School")

s1.show()
        
    