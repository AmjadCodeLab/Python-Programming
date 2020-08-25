#Default Argument
class Test:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("Sum of Test " , a+b+c)
        elif a!=None and b!=None:
            print("Sum of Test ",a+b)
        else:
            print("Please provide 2 and 3 Variable")

t=Test()
t.sum(10,20)
t.sum(30,40,50)
t.sum()
t.sum(10)

#Variable Number of Argument
class Test1:
    def sum(self,*n):
        total=0
        for n1 in n:
            total=total+n1
        print("The Sum of Test1 ", total)

t1=Test1()
t1.sum()
t1.sum(20)
t1.sum(10,30)
t1.sum(30.40,50)