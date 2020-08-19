class Father:
    def Height(self):
        print("Height is 6 Feet")
    
class Mother():
    def Color(self):
        print("Color is Brown")

class Child(Father,Mother):
    pass

c=Child()
print("Child Inherited the Properties from Parents")
c.Height()
c.Color()


#################**********************################


class P1:
    def m1(self):
        print("P1 Method")

class P2:
    def m1(self):
        print("P2 Method")

""" class C(P1,P2):
    pass

c=C()
c.m1() """


class C(P2,P1):
    pass

c=C()
c.m1()