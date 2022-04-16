# Program to calculate the factorial of a number
num=int(input("Enter a number :"))
fact=1
a=1
while a<= num:
    fact*=a                                                                          # fact = fact*a
    a+=1                                                                             # a = a+1
print("The factorial of", num,"is",fact)
