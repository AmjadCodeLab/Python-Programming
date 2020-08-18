def isEven(n):
    if n%2==0:
        return True
    else:
        return False

l=[1,2,3,4,5,6,7,8,9,10]
l1= list(filter(isEven,l))
print(l1)

   # Or using lambda Function

l2= list(filter(lambda x: x%2==0,l))
print(l2)


# Similary for Odd Number

l3=list(filter(lambda x: x%2!=0,l))
print(l3)

