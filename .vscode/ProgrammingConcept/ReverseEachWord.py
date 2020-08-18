# Using for loop

name = input("Enter the String::")

s= name.split()
print(s)
li=[]
for x in s:
    li.append(x[::-1])
    output = ' '.join(li)
print(output)
