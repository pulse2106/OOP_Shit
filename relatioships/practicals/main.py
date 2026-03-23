
class Car:

    engine=None
    passangers=None

    def __init__(self):

        ### create standard engine. 800cc
        self.engine=Engine()        #### HAS-A --> composition

        self.passangers=[]  #### HAS-A lose relationsip --> aggregation

    def add_passenger(self,pPassenger):
        self.passangers.append(pPassenger)
        
    def remove_passenger(self,pPassenger):
        self.passangers.remove(pPassenger)

    def Check_Engine(self):
        print("engine ",self.engine,"checked")

    def Start(self):
        pass   

class Engine:
    def __init__(self):
        pass

class TurboEngine(Engine):
    def __init__(self):
        pass

class Passengers:
    pass

class Ferrari(Car):
    def __init__(self): #### override
        self.engine=TurboEngine()
    
    def __init__(self,pCapacit):     ####  overload
        self.engine=TurboEngine()
        self.capacity=pCapacit
    
    def Start(self):
        self.Check_Engine()
        print("start Ferari")
        

fi=Ferrari()
f2=Ferrari(2.0)
