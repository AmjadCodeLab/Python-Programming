#Sort the Alphanumeric String

name = input("Enter the String")
s1=s2=output='' #""" Taken 3 Variable s1 s2 and output as empty"""
for x in name:
    if x.isalpha():
        s1=s1+x
        print(s1)
    else:
        s2=s2+x
        print(s2)
for x in sorted(s1):
    output=output+x
for x in sorted(s2):
    output=output+x
print(output)
