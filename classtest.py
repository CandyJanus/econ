class thing:
    def __init__(self):
        self.number=5
        self.thingBegin()
    def thingBegin(self):
        print(self.number)  
    def thingSelfMult(self, multVar):
        self.number=self.number*multVar
        print(self.number)
        
a=thing()
a.thingSelfMult(2)
     