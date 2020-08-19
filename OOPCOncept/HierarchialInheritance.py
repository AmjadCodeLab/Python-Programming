class Parent:
    def m1(self):
        print("Parent Method")

class Child1(Parent):
    def m2(self):
        print("Child One")

class Child2(Parent):
    def m3(self):
        print("Child Two")

c1=Child1()
c1.m1()
c1.m2()

c2=Child2()
c2.m1()
c2.m3()
