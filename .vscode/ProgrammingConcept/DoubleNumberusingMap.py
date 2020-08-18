#Using map() double the number

def square(n):
    return n*2

l=[10,20,30,40,50]
l1=list(map(square,l))
print(l1)

   # Using Lambda Function

l2= list(map(lambda x: x*2,l))
print(l2)

# Multiply each content of two list

l3=[1,2,3,4,5]
l4=[10,20,30,40,50]
l5=list(map(lambda x,y: x*y,l3,l4))
print(l5)