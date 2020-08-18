class Animal:
    legs=4
    @classmethod
    def walk(cls,name):
        print("{} has {} legs".format(name,cls.legs))

Animal.walk('Horse')
Animal.walk("Tiger")

#How to track the number of Object crearted for a class

class Test:
    count=0
    def __init__(self):
        Test.count=Test.count+1
    @classmethod
    def noOfObjects(cls):
        print("The Number of Object Created ",cls.count)

t1=Test()
t2=Test()
t4=Test()
t3=Test()
t4=Test()
Test.noOfObjects()