class Parent:
    def m1(self):
        print("Parent Method")
    
class Child(Parent):
    def m2(self):
        print("Child Method")

c=Child()
c.m1()
c.m2()