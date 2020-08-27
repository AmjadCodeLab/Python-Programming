#finditer
print("############### FindIter Function ###############")
import re
matcher = re.finditer('ab','abaabaaba')
count=0
for m in matcher:
    count=count+1
    print("Match Index at",m.start())
    print(m.start(),'...',m.end(),'...',m.group())
print("No of occurance of pattern", count)

print("############### Match Function ###############")
#match
s="Python learning is good for all"
m=re.match('lesson',s)
if m!=None:
    print("Match at begining of the String")
    print(m.start(),'...',m.end())
else:
    print("Match is not Available at Begining")

print("############### FullMatch Function ###############")

s="Python is Good For Every One"
m=re.fullmatch("Python is Good For Every One",s)
if m!=None:
    print("Full String Matched")
else:
    print("No String Matched")

print("############### Search Function ###############")

s="Python is Very Good"
m=re.search('Python',s)
if m!=None:
    print("Matched is Available")
    print("First occurance {} and end occurance {}".format(m.start(),m.end()))
else:
    print("Full String Not Matched ")


print("############### FindAll Function ###############")

l=re.findall('[0-9]','a7b9k6z')
print(l)