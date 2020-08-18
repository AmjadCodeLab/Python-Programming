#First Example

class Student:
    '''Documnetation Info '''
    def __init__(self,n='',m=0):    #Here __init__ is used to declare constructor
        self.name=n
        self.mark=m
    def display(self):
        print("Hi : ",self.name)
        print("Marks : ",self.mark)

#Create Object

s1= Student()
s1.display()

s2=Student('Amjad',100)
s2.display()

#Second Example
class Employee:
    def __init__(self,name,id,addr):
        self.name=name
        self.id=id
        self.addr=addr
    
    def Display(self):
        print("Employee Name : ",self.name)
        print("Employee Id : ",self.id)
        print("Employee Address : ",self.addr)

e1=Employee("Amjad",7,"Jatani")
e1.Display()