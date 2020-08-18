#Passing members of one class to another class
class Employee:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal

    def display(self):
        print("Employee ID ",self.id)
        print("Employee Name ",self.name)
        print("Employee Salary ",self.sal)

""" class Test:
    def modify(emp):
        emp.sal=emp.sal+800
        emp.display()

e = Employee(10,'Amjad',7000)
Test.modify(e) """