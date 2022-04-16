num=int(input("Enter a number : "))
n=num
res=0
while num>0:
    rem=num%10
    res=rem+res*10
    num=num//10
if res==n:
    print(res,"is a Palindrome")
else:
    print(res,"is not a Palindrome")
