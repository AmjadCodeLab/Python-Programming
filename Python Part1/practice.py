n = int(input("Number of Student:: "))
rec={}
i=1
while i<=n:
    Name=input("Enter Student name: ")
    Mark=input("Enter % Mark:: ")
    rec[Name] = Mark
    i=i+1
print("Name of the Student ","\t" ,"% Mark Obtained")
for x in rec:
    print("Name :: ",x,"\t\t","% Mark :: ",rec[x])

word = input("The Word")
s=set(word)
vowels={'a','e','u','o','i'}
result = s.intersection(vowels)
print(result) 

s=set('amjadali')
print(s)

s={10,20,30}
s.add(60)
print(s)

l=[10,30,55,66]
s.update(l)
print(s)

s.pop()
print(s)

s.remove(10)
print(s)

s.discard(20)
print(s)
s.discard(120)
print(s)

s1={10,20,30}
s2={30,40,50}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))
print(s2.difference(s1))


d={}
print(type(d))

list=[5,4,8,2,80]

for i in range(0,len(list),1):
    next=-1
    for j in range(i+1,len(list),1):
        if list[i] < list[j]:
            next= list[j]
        break
    print(str(list[i]),"....",str(next))


s= {x*x for x in range(1,5)}
print(s)

d={10:'amjad',11:'ali',12:'sk'}
print(d)

d[10]='web' 
#print(d.clear())

print(d.get(10))
print(d.get(14,'amjad'))

d.pop(10)
print(d)

d.popitem()
print(d)

del d[11]
print(d)

dic = {1:'a',2:'b',3:'c',4:'d'}
print(dic.keys())
print(dic.values())
di ={5:'e'}
dic.update(di)
print(dic)

print(dic.items())
for k,v in dic.items():
    print(k,"....",v)

#number of occurence of vowel in string

word='brown dog jump over fox to catch the fish'
vowels = {'a','e','i','o','u'}
d={}
for x in word:
    if x in vowels:
        d[x]=d.get(x,0)+1
print(d)
for k ,v in sorted(d.items()):
    print("{} occurs {} time".format(k,v))


n=int(input("Enter number of student :: "))
d={}
for i in range(n):
    name=input("Enter Student Name : ")
    mark=input("Enter Student Mark : ")
    d[name]=mark
while True:
    name=input("Enter Student name for Mark :: ")
    mark=d.get(name,-1)
    if mark==-1:
        print("Student Name is not Available in List ")
    else:
        print("Student {} has secured mark {}".format(name,mark))
    option=input("Do you want any other Student mark")
    if option=="No":
        break
print("Thanks for using Our Student Portal App")


#LOCAL AND GLOBAL VARIABLE

a=10
def f1():
    global a
    a=20
    print(a)
def f2():
    global a
    a=30
    print(a)
def f3():
    print(a) 

f3()
f1()
f2()

def f4():
    a=20
    print(a)
    print(globals()['a'])

f4()

#lambda function or Anonymous function
#Square of Number
s= lambda n:n*n
print(s(3))

#Addition of 2 Number
s=lambda a,b: a+b
print(s(10,30))


# reduce()
from functools import reduce
l=[10,20,30,40,50]

result = reduce(lambda x,y: x+y,l)
print(result)


#Function Aliasing

def wish(name):
    print("Hello",name,"Good Morning")

greeting=wish
greeting('Amjad')

#Nested Function concept

def outer():
    print("This is Outer function")
    def inner():
        print("This is Inner Function")
    inner()

outer()

#Function Decorator
#handling zerodivision error using decorator function concept

def smartdivison(func):
    def inner(a,b):
        if b==0:
            print("Zero Divison Not Possible")
        else:
            return func(a,b)
    return inner

@smartdivison
def division(a,b):
    return a/b

print(division(10,2))
print(division(10,0))
print(division(10,5))

#Another Decorator example

def decor(func):
    def inner(name):
        if name=='ali':
            print("hello ali you are most welcome to learn both python and javascript")
        else:
            return func(name)
    return inner

def decor1(func):
    def inner(name):
        if name=='amjad':
            print("Hello amjad you are welcome to learn any programming knowledge")
        else:
            return func(name)
    return inner

@decor
@decor1
def greet(name):
    print("Hello",name,"You are welcome to Python Class")

greet('amjad')


#Decor Chaining Concept example 2

def decor2(func):
    def inner(name):
        print("First Decor")
        return func(name)
    return inner

def decor3(func):
    def inner(name):
        print('Second Decor')
        return func(name)
    return inner
@decor2
@decor3
def wwishperson(name):
    print("Hello",name,"Good Morning")

wwishperson('anna')

#Generator Concept
#find the first n number
def firstn(num):
    n=1
    while n<=num:
         yield n
         n=n+1
value=firstn(7)
for x in value:
    print(x)

#Using Math Function
from random import *
list=['amjad','ali','sk']
for i in range(5):
    print(random())
    print(randint(1,10))
    print(uniform(1,10))
    print(randrange(1,10,2))
    print(choice(list))

#Program to print 6 digit number as OTP
for x in range(10):
    print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')

#Program to Print 6 digit Alphanumeric Random Password:
for x in range(10):
    print(chr(randint(65,65+25)),randint(0,9),chr(randint(65,65+25)),randint(0,9),chr(randint(65,65+25)),randint(0,9),sep='')


try:
    x=int(input("Enter number1::"))
    y=int(input("Enter number2::"))
    print(x/y)
except ArithmeticError as msg:
    print("This is invalid input reason is :: ",msg)
except ValueError as msg:
    print("This is invalid reason is :: ",msg)
finally:
    print("Process the code and close the program")

