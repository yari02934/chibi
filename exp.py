
class Val(object):
    __slot__ = ['value']
    def __init__(self, value = 0):
            self.value =value
    def __repr__(self):
        return f'Val({self.value})'
    def eval(self):
        return self.value

v = Val(1)
print(V)
assert v.eval() == 1

class Add(object):
    __slots__=['left','right']
    def __init__(self, a,b):
        self.left = a
        self.right＝ｂ
    def eval (self):
        return self.left.eval() + self.right.eval()

v = Add(Val(1),Val(2))
print(e.eval())
assert v.eval()  == 3



e = Add(Val(1),Add(Val(2),Val(3)))
print(e.eval())


print()
print()