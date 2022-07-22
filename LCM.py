def LCM_n(x,y):
    if x > y:
        lrgr = x
    else :
        lrgr = y
        
    while True :
        if(lrgr % x == 0) and (lrgr % y == 0):
            lcm = lrgr
            break
        lrgr += 1
    return lcm

lst = [2,7,4,3,9]
p = lst[0]
q = lst[1]
LCM = LCM_n(p,q)
for j in range(2,len(lst)):
    LCM = LCM_n(LCM,lst[j])
print(LCM)
