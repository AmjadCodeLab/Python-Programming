# Remove duplicate element in String

s= eval(input("Enter the String:: "))

#using for loop
l=[]
for x in s:
    if x not in l:
        l.append(x)    
print(l)
print(''.join(l))

#Using Set() one line only but insertion order is not preserved
print(''.join(set(s)))
