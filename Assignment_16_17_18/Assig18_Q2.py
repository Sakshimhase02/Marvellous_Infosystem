def Maximum(Data):
    Max = Data[0]

    for No in Data:
        if No > Max:
            Max = No

    return Max

def main():

    Size = int(input("Enter number of elements: "))

    Data = []

    print("Enter the elements:")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Ans = Maximum(Data)

    print("Maximum number is:", Ans)

if __name__ == "__main__":
    main()