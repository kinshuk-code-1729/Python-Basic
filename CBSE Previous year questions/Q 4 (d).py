class Stock :
    def __init__(self,N,P):
        self.Name=N
        self.Price=P
    def Show(self):
        print(self.Name,"@",self.Price)
