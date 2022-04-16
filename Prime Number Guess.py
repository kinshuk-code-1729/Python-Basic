num=int(input("Enter the number: "))
chk=0
for i in range(1,num+1):
    if num%i==0:
        chk+=1
if chk==2:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")
