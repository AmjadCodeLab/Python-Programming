class Student:
    def setName(self,name):
        self.name=name
    
    def getName(self):
        return self.name
    
    def setMark(self,marks):
        self.marks=marks

    def getMark(self):
        return self.marks
    
n=int(input("Enter Number of Student : "))
for i in range(n):
    s=Student()
    names=input("Enter Student Name : ")
    s.setName(names)
    marks= int(input("Enter the Marks : "))
    s.setMark(marks)

    print("Hi ",s.getName())
    print("Mark Secured By You ",s.getMark())
