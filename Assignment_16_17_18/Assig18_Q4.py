def Frequency(Data, No):
    Count = 0

    for Value in Data:
        if Value == No:
            Count = Count + 1

    return Count

def main():

    Size = int(input("Enter number of elements: "))

    Data = []

    print("Enter the elements:")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Search = int(input("Enter element to search: "))

    Ans = Frequency(Data, Search)

    print("Frequency is:", Ans)

if __name__ == "__main__":
    main()