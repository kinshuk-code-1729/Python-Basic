s=input("Enter Word: ")
l=len(s)
m=l/2
r=-1
for x in range(m):
    if s[x]==s[r]:
        x +=1
        r -=1
    else:
        print(s,"isn't  a palindrome")
        break
else:
    print(s,"is a palindrome")
