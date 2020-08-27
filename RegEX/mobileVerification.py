import re
s=input('Enter a Valid Mobile Number')
m=re.fullmatch('[6-9]\d{9}',s)
if m!=None:
    print(s,"Is Valid Mobile Number")
else:
    print(s,"Is not a valid Number")