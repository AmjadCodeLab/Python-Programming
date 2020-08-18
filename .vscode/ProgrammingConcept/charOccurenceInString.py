# Check for the Char Occurence or Repeate in String

#note to check for the duplicate occurance go for dict concept { key , value} pair

s = input("Enter the String :: ")
d={}
for x in s:
    if x not in d.keys():
        d[x]=1
    else:
        d[x]= d[x]+1
for k,v in d.items():
    print("{} occurs {} times ".format(k,v))


