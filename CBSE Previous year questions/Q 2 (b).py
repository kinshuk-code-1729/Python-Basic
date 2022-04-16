class Box:
    L = 10
    Type="HARD"
    def __init__(self,T,TL=30):
        self.Type = T
        self.L    = TL
    def Disp(self):
        print (self.Type,Box.Type)
        print (self.L,Box.L)
B1=Box("SOFT",20)
B1.Disp()
Box.Type="FLEXI"
B2=Box("HARD")
B2.Disp()
