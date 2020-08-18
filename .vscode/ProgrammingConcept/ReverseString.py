
#Reverese the content and word of string

name = input("Enter the string::")
#Genric Way using Slice Operator 
print(name[::-1])

# Using reversed() method
print(''.join(reversed(name)))

#Using both reveresed and for loop
for x in reversed(name):
    print(x,end='')
print()

#Using While Loop
result=""
l = len(name)-1
while l>=0:
    result=result+name[l]
    l = l-1
print(result)

