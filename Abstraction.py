class Car():
    
    def __init__(self):
        self.accelerator=False
        self.brk=False
        self.clutch=False
    def start(self):
          self.accelerator=True
          self.brk=True
          self.clutch=True
car1=Car()
car1.start
                
        