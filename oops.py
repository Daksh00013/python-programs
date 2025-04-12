class Student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def get_avg(self):
        sum=0
        total=500
        for value in self.marks:
            sum+=value
        print("hi",self.name,"your percentage score is:", (sum/total)*100)
        
s1=Student("karan",[67,78,98])
s2=Student("daksh",[78,78,78,54,87])
s3=Student("jiya",[100,85,79,71,84])
s3.get_avg()
