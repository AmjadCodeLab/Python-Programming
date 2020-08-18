class Parent:
    a=10
    def m1(self):
        print("Parent Class Instance Method")
    @classmethod
    def m2(cls):
        print("Parent Class Class Method")

    @staticmethod
    def m3():
        print("Parent Class Static Method")

    def __init__(self):
        print("Parent Class Constructor..")

    def __del__(self):
        print("Parent Class Destrcutor..")

class Child(Parent):
    pass

c=Child()
print(c.a)
c.m1()
c.m2()
c.m3()

    