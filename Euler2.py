C = 0
class Fib():
    X1 = 0
    X2 = 1
    Y1 = 1
    @classmethod
    def Next(cls):
        cls.Y1 = cls.X1 + cls.X2
        cls.X2 = cls.X1
        cls.X1=  cls.Y1
        return cls.Y1
    @classmethod
    def Reset(cls):
        cls.Y1, cls.X1, cls.X2 = 1, 0, 1
X = 0
while Fib.Y1 < 4000000:
    if Fib.Y1 % 2 == 0:
        X += Fib.Y1
    Fib.Next()
print(X)
