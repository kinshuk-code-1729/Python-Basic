def addloc(cmp):
    dd=cmp[0:2]
    ln=len(planned)
    if ln==0:
        planned.append(cmp)
    else:
        last=planned[ln-1]
        if int(dd)>=int(last[0:2]):
            planned.append(cmp)
        else:
            for i in range(ln):
                cp=planned[i]
                if int(dd)<=int(cp[0:2]):
                    planned.insert(i,cmp)
                    break
def conductCamp(cmp):
    conducted.append(cmp)
    planned.remove(cmp)
def search(cmp,lst):
    ln=len(lst)
    for i in range(ln):
        if cmp in lst[i]:
            return lst[i]
        else:
            return False
def Report():
    lenp=len(planned)
    lenc=len(conducted)
    print("\tREPORT")
    print("------------------------------------------")
    print("Camps conducted so far : ",lenc)
    print("People served so far :",ppl)
    print("Camps to be conducted : ",lenp)
    print("------------------------------------------")
def display():
    print("\nCamps Conducted so far : ",end=' ')
    for i in planned:
        print(i,end=',')
    print(". . . ! !")
#__main__
planned=[]
conducted=[]
ppl=0
ch=0
while (ch !=6):
    print("\t---------")
    print("\tMENU")
    print("\t---------")
    print("1. Add Camp Location")
    print("2. Camp Conducted")
    print("3. Look for a Camp")
    print("4. Report")
    print("5. Display List")
    print("6. Exit")
    ch=int(input("Enter your choice (1-6): "))
    if ch==1:
        cm=input("Enter Camp location : ")
        dd=input("Enter date of the month(only dd): ")
        cmp=dd+cm
        addloc(cmp)
    elif ch==2:
        cm=input("Camp conducted at location? ")
        p=int(input("How many people are served at this camp?"))
        ppl=ppl+p
        result=search(cm,planned)
        if result ==False:
            print("Sorry no such camp in the list")
        else:
            conductCamp(result)
    elif ch==3:
        cm=input("Enter camp location : ")
        r1=search(cm,planned)
        if r1==False:
            r2=search(cm,conducted)
            if r2==False:
                print("Sorry no such camp in our list")
            else:
                dd=r2[0:2]
                print(cm,"camp was conducted on date",dd,"of this month")
        else:
            dd=r1[0:2]
            print(cm,"camp is to be conducted on date",dd,"of this month")
    elif ch==4:
        Report()
    elif ch==5:
        display()
    elif ch !=6:
        print("Wrong choice ! Enter choice from 1 to 6 only")
else:
    print("THANK YOU")
