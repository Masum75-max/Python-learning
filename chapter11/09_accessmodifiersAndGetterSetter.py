class bank:
    def __init__(self,name,balance,pin):
        
        self.myName=name
        self._myBalance=balance
        self.__myPin=pin
    
    def  get(self,pin):
        if(self.__myPin==pin):
            print("your balance is ",self._myBalance)
            
        else:
            print("Invalid pass")
    
    def set(self,pin,bal):
        if(self.__myPin==pin):
            self._myBalance+= bal
        else:
            print("invalid pass")

acc1 = bank("masum",100,33221)

acc1.get(33221)
acc1.set(33221,200)
acc1.get(33221)