import random

VALUES=[10,20,30,40,50,60,70,80]
BEGIN=random.randint(1,3)
LAST=random.randint(BEGIN,4)

for I in range(BEGIN,LAST+1):
    print(VALUES[I],"-",)
