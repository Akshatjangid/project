class car:
    def __init__(self):
        car.clh=False
        car.acc=False
        car.brk=False
    
    def start():
        car.clh=True
        car.acc=True
        print("car started...")

car1=car
car1.start() # type: ignore
