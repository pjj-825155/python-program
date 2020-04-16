class b:
    def __init__(self,e):
        self.e=e
    def f(self,m):
        print(m)
    def ff(self,m):
        self.f(m)
        self.f(self.e)
