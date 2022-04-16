Ph_no=input("Enter Phone Number : ")
def Checkno(n):
    if len(n)!=12:
        return False
    if n[3]!='-':
        return False
    n=n[:3]+n[4:]
    if n[6]!='-':
        return False
    n=n[:6]+n[7:]

    return n.isdigit()
if Checkno(Ph_no):
    print("The given phone number is valid")
else:
    print("INVALID INPUT PLEASE ENTER VALID phone number of 10 digits")
