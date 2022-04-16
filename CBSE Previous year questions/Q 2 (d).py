class Furniture(object):
    def __init__(self,TQ):
        self.Qty = TQ
    def GetMore(self,TQ):
        self.Qty =self.Qty+TQ
    def FRDisp(self):
        print(self.Qty)

class Fixture(object):
    def __init__(self,TQ):
        self.Qty=TQ
    def GetMore(self,TQ):
        self.Qty =self.Qty+TQ
    def FRDisp(self):
        print(self.Qty)

class Flat(Furniture,Fixture):
    def __init__(self,fno):
        self.Fno=fno
        TQ=0
        if self.Fno<100:
            TQ=10
        else:
            TQ=20
        Furniture.__init__(self,TQ)
        Fixture.__init__(self,TQ)
    def More(self,TQ):
        Furniture.GetMore(self,TQ)
        Fixture.GetMore(self,TQ)
    def FLDisp(self):
        print(self.Fno,)
        Furniture.FRDisp(self)
        Fixture.FRDisp(self)

FL=Flat(101)
FL.More(2)
FL.FLDisp()
