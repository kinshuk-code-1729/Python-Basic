def Changer(P,Q=10):
    P=P/Q
    Q=P%Q
    print (P,"#",Q)
    return P
A=200
B=20
A=Changer(A,B)
print (A,"$",B)
B=Changer(B)
print (A,"$",B)
A=Changer(A)
print (A,"$",B)
