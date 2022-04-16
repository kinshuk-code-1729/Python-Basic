L=eval(input("Enter the elements: "))
n=len(L)
item=eval(input("Enter the element that you want to search : "))
for i in range(n):
    if L[i]==item:
        print("Element found at the position :", i+1)
        break
    else:
        print("Element not Found")
