Msg1="WeLcOME"
Msg2="GUeSTs"
Msg3=""
for I in range(0,len(Msg2)+1):
    if Msg1[I]>="A" and Msg1[I]<="M":
        Msg3=Msg3+Msg1[I]
    elif Msg1[I]>"N" and Msg1[I]<="Z":
        Msg3=Msg3+Msg2[I]
    else:
        Msg3=Msg3+"*"
print(Msg3)
