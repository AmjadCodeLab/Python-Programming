# using slice opperator to define even and odd strings

name = input("Enter the string :: ")

print("Char at even indexs of String: ",name[::2])
print("Char at odd indexs of String: ",name[1::2])

#Using loop

i=0
print("Characters at even places: ")
while i<len(name):
    print(name[i],end='')
    i=i+2
print()
j=1
print("Character at odd places: ")
while j<len(name):
    print(name[j],end='')
    j=j+2
print()