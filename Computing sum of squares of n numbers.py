def sqsum(n):
    if n==1:
        return 1
    return n*n+sqsum(n-1)
#__main__
n=int(input("Enter value of n :"))
print(sqsum(n))
