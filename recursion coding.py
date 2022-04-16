def out(n):
    if(n==0):
        return
    else:
        out(n-1)
        print(n)
n=6
out(n)
