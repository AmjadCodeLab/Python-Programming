name = input("Enter the String")

#using reveresed method
s = name.split()
reverse = ' '.join(reversed(s))
print(reverse)

#Using Loop

s1= name.split()
li=[]
i=len(s1)-1
while i>=0:
    li.append(s1[i])
    i=i-1
    output=' '.join(li)
print(output)