class Target:
    def __init__(self):
        self.X = 20
        self.Y = 24
    def Disp(self):
        print(self.X,self.Y)
    def __del__(self):
        print("Target Moved")
def One():
    T=Target()
    T.Disp()
One()
