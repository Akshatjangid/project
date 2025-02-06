class car:
   color="black"
   @staticmethod
   def start():
      print("Car Started...")

   @staticmethod
   def stop():
      print(" Car stopped...")
class toyota(car):
   def __init__(self,name):
      self.name=name

car1=toyota("fortuner")
car2=toyota("innova")
print(car1.name)
print(car1.color)
print(car2.name)
print(car1.color)