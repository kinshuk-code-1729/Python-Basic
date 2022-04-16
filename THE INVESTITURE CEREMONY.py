def select_errors(STL):
    newList=[]
    for record in STL:
        name_surname=record.split(' ')
        name=name_surname[0]
        surname=name_surname[1]
        if name[0].islower() or surname[0].islower():
            newList.append(record)
    return newList

def select_correct(STL):
    newList=[]
    for record in STL:
        name_surname=record.split(' ')
        name=name_surname[0]
        surname=name_surname[1]
        if not name[0].islower() and not surname[0].islower():
            newList.append(record)
    return newList

def correct_entries(STL):
    newList=[]
    for record in STL:
        name_surname=record.split(' ')
        name=name_surname[0]
        surname=name_surname[1]
        newList.append(name.capitalize()+' '+surname.capitalize())
    return newList

#__main__
STL=[]
ch=0
while (ch !=4):
    print("\t---------")
    print("\tMENU")
    print("\t---------")
    print("1. Apply for the School Post")
    print("2. List of all applicants")
    print("3. Correct the Incorrect Entries")
    print("4. Exit")
    ch=int(input("Enter your choice (1-4): "))
    if ch==1:
        name=input("Enter your name : ")
        STL.append(name)
    elif ch==2:
        print("Students applied so far: ")
        print(STL)
    elif ch==3:
        ok_entries=select_correct(STL)
        error_entries=select_errors(STL)
        corrected_entries=correct_entries(STL)
        print("Correctly entered names:",ok_entries)
        print("Incorrectly entered names:",error_entries)
        print("Corrected names :",corrected_entries)
    elif ch !=4:
        print("Sorry ! Valid choices are 1 to 4:")
    else:
        print("THANK YOU")
