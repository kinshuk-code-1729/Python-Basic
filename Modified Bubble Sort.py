L=eval(input("Enter the elements:"))
n=len(L)
for p in range(0,n-1):
    for i in range(0,n-1):
        if L[i]>L[i+1]:
            t=L[i]
            L[i]=L[i+1]
            L[i+1]=t
print("The sorted list is : ", L)
