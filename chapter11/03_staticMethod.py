class student:
    school_name="ABC school"
    
    def __init__(self,name):
        self.name=name
        
    @classmethod
    
    def change_school_name(cls,name):
        cls.school_name = name
        
    
    @staticmethod
    
    def is_holidy(day):
        if("friday"==day.lower()):
            return  True
        
s1 =  student("masum")

if(s1.is_holidy("friday")):
    print("colo sinama deki")
    
else:
    print("potte hobee , nokol r hobe naa")
        
    