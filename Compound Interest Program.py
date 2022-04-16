p=float(input("Enter the principal amount : "))
r=float(input("Enter the rate of interest : "))
t=float(input("Enter the time in years : "))

x=(1+r/100)**t

CI= p*x-p
print("Compound interest is : ", round(CI,2))
