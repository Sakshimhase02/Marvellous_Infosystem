def Addition(Data):
    Sum = 0

    for No in Data:
        Sum = Sum + No

    return Sum

def main():

    Size = int(input("Enter number of elements: "))

    Data = []

    print("Enter the elements:")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Ans = Addition(Data)

    print("Addition is:", Ans)

if __name__ == "__main__":
    main()