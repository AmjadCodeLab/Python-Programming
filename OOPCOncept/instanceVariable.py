class Student:
    def __init__(self,name,rollno):
        self.a=10
        self.name=name
        self.rollno=rollno
    
    def display(self):
        self.b=1000
        self.c=2000
        print("Student",self.name)
        print("Roll no",self.rollno)

s1=Student('amjad',77)
s1.display()
print(s1.a)
print(s1.name,s1.rollno)
s1.a=88
print(s1.a)
print(Student.__dict__)
