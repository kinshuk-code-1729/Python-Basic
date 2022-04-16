def Out_upto(n):
    if n==0:
        return
    else:
        Out_upto(n-1)
        print(n)
#__main__
Out_upto(4)
