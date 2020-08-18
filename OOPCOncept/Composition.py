class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    
    def getCarInfo(self):
        print("Car name {} and model {} with {} color".format(self.name,self.model,self.color))

class Employee:
    def __init__(self,ename,eno,car):
        self.ename=ename
        self.eno=eno
        self.car=car
    def getEmpInfo(self):
        print("Employee Name : ",self.ename)
        print("Employee No : ",self.eno)
        print("Employee Car Details")
        self.car.getCarInfo()

c=Car('Honda','Amaze','Blue')
e=Employee('Amjad',7,c)
e.getEmpInfo()