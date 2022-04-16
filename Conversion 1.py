def feetToInches(n):
    return n*12

def inputFeet():
    return float(input("Enter height in feet : "))

def displayInches(inches):
    print("The height in inches is",inches)

displayInches(feetToInches(inputFeet()))
