#repeat the char based on output 
# a3b2 ==> aaabb

name = input("Enter the string: ")
output=''
for x in name:
    if x.isalpha():
        output=output+x
        previous=x
    else:
        output=output+previous*(int(x))
print(output)