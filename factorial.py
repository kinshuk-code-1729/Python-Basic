def factorial(x):
    fact=n
    for i in range(1,x):
        fact=fact*i
    return fact

n=int(input("Enter a number (>0):"))
print("Factorial of",n,"is",factorial(n))
