#add char of each subsequent from 2 string
#input1-> amjadali ,input2->  ali , output-> aamljiadali

n1 = input("Enter the First String:: ")
n2 = input("Enter the Second String:: ")

output=''

i=j=0

while i<len(n1) or j<len(n2):
    if i<len(n1):
        output = output+n1[i]
        i=i+1
    if j<len(n2):
        output=output+n2[j]
        j=j+1
print(output)