class GF:
    def m1(self):
        print("Grand Father")

class F(GF):
    def m2(self):
        print("Father")

class C(F):
    def m3(self):
        print("Son")

c=C()
c.m1()
c.m2()
c.m3()
    