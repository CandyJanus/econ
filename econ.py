
# depreciate and remove? not sure why I'd need a worldCreator when I can just init world, don't think I need factory pattern
# class WorldCreator:
    # def __init__(self, ):
        # self.numCities=numCities
        # self.world=createWorld(numcities)
                         
    # def createWorld(numCities):
        

class World:
    def __init__(self, numCities):
        cityList=self.cityListGenerator(numCities)
        
    def cityListGenerator(self, numCities):
        #cityList=[None]*numCities
        for i in range(numCities):
            #ids each city by number
           cityList[i]=City(i, 1,1)
        return cityList
        
        
        #Superloop()
        
    # def Superloop()
        # while
            # timeTick
        
    #to implement
    
    #def timeTick():
    #call all the cities internal timetick economic functions
    
    

class City:
    def __init__(self, id, pop, wealth):
        self.id=id
        self.pop = pop
        self.wealth= wealth
        
    # def printStats(self)"
        # print()
        
    
# a1=City(1,1)
# print(a1.pop)
    
# b2=Default

World(2)

