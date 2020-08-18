def Factorial(n):
#Factorial Function to find factorial of number n in paramenter
    fact=1
    while n>=1:
        fact = fact*n
        n=n-1
    return fact

print(Factorial(5))
print(Factorial(6))

