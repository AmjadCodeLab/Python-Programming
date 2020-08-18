#Find the Unique vowwels in the given word

vowels=['a','e','i','o','u','A','E','I','O','U']

word = input("enter the word :: ")
found=[]
for letter in word:
    if letter.lower() in vowels:
        if letter.lower() not in found:
            found.append(letter.lower())
print(found)
print("The Number of total vowle found :: ",len(found))