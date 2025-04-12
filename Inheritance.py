class car:
    @staticmethod
    def start():
        print("car satrted")
    @staticmethod
    def stop():       
        print("car stopped")
class ToyotoCAr(car):
    def __init__(self,name):
        self.name=name
        
car1=ToyotoCAr("fortuner")
car2=ToyotoCAr("innova")

print(car1.name)