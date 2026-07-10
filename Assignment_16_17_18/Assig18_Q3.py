def Minimum(Data):
    Min = Data[0]

    for No in Data:
        if No < Min:
            Min = No

    return Min

def main():

    Size = int(input("Enter number of elements: "))

    Data = []

    print("Enter the elements:")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Ans = Minimum(Data)

    print("Minimum number is:", Ans)

if __name__ == "__main__":
    main()

