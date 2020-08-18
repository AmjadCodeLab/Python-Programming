#find the next char based on number
#input - a3b2 ===> aebd

name = input("Enter the String:: ")
output=''
for x in name:
    if x.isalpha():
        output=output+x
        previous=x
    else:
        newchar =chr(ord(previous)+int(x))
        output=output+newchar
print(output)