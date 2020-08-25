class Book:
    def __init__(self,pages):
        self.pages=pages
    
    def __lt__(self,other):
        return self.pages<other.pages

    def __ge__(self,other):
        return self.pages>=other.pages

b1=Book(2000)
b2=Book(3000)

print("Less Pages ", b1<b2)
print("Less Pages",b1>b2)
print("Greater than Equal ",b1>=b2)
print("Greater than Equal ", b1<=b2)