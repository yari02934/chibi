class Q(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __repr__(self):
        if self.b ==1:
            return str(self.a)
        return f'{self.a}/{self.b}'

q = Q(3)
print(q)