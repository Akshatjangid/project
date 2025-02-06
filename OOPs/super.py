class car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("car started ...")

    @staticmethod
    def stop():
        
        print("car stopped ...")
    
class toyota(car):
    def __init__(self,color,type):
        super().__init__(type)
        self.color=color
        super().start()
        super().stop()
        
       

car1=toyota("Fortuner","black")
print(car1.color)
print(car1.type)