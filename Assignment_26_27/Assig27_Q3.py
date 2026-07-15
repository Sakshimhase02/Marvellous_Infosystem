class Numbers:

    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):

        if self.Value <= 1:
            return False

        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False

        return True

    def ChkPerfect(self):

        Sum = 0

        for i in range(1, self.Value):
            if self.Value % i == 0:
                Sum = Sum + i

        if Sum == self.Value:
            return True
        else:
            return False

    def Factors(self):

        print("Factors are :")

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i)

    def SumFactors(self):

        Sum = 0

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                Sum = Sum + i

        return Sum


Obj1 = Numbers(28)
Obj2 = Numbers(17)

print("Object 1")
print("Prime :", Obj1.ChkPrime())
print("Perfect :", Obj1.ChkPerfect())
Obj1.Factors()
print("Sum of Factors :", Obj1.SumFactors())

print()

print("Object 2")
print("Prime :", Obj2.ChkPrime())
print("Perfect :", Obj2.ChkPerfect())
Obj2.Factors()
print("Sum of Factors :", Obj2.SumFactors())