class Student():
    
    def __init__(self,fullname,marks):
        self.name=fullname
        self.don=marks
        print("adding new student in database")
        
s1= Student("karan",67)
print(s1.name, s1.don)
s2=Student("arjun",56)
print(s2.name, s2.don)
 