import json as j
Length = 0
def Convert(n):
    StrNums = j.load(open("euler17/Nums.json"))
    def Ones():
        Num1 = str(n)
        return StrNums[Num1]
    def Twos():
        Num1 = str(n)[-1]
        Num2 = str(n)[-2] + "0"
        return StrNums[Num2] + StrNums[Num1]
    def Threes():
        Num1 = str(n)[-1]
        Num2 = str(n)[-2]
        Num3 = str(n)[0]
        if Num2 + Num1 == "00": return StrNums[Num3]+"hundred"
        if Num2 == "0":return StrNums[Num3] + "hundredand"+StrNums[Num1] 
        if Num2 == "1": return StrNums[Num3] +'hundredand' + StrNums[Num2 + Num1]
        return StrNums[Num3] + "hundredand" + Twos()
    if n < 20: return Ones()
    if n < 100: return Twos()
    if n < 1000: return Threes()
    return "onethousand"
LEN = 0
for x in range(1, 1001):
    LEN += len(Convert(x))
print(LEN)
