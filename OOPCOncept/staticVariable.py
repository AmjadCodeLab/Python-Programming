class Test:
    a=10
    def __init__(self):  #Instance Varibale inside constructor
        self.b=20
        self.c=30
    
    def m1(self):
        self.d=40
        Test.e=50
    
    @classmethod
    def m2(cls):
        cls.f=60
        Test.g=70
    
    @staticmethod
    def m3():
        Test.h=80

t=Test()
t.m1()
t.m2()
t.m3()
print(Test.__dict__)

class Demo:
    a=10
    def __init__(self):
        self.b=20

t1=Demo()
t2=Demo()
t1.a=77
t1.b=88
print(t1.a,t1.b)
print(t2.a,t2.b)
print(t1.__dict__)
print(t2.__dict__)
t2.a +=1
print(t2.a)