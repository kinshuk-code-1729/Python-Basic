#Function for calculating factorial of a number using return
def fact(num):
    result = 1
    while num >= 1:
        result = result * num
        num = num - 1
    return result
for i in range(1,25):
    print("The factorial of",i,"is ",fact(i))
