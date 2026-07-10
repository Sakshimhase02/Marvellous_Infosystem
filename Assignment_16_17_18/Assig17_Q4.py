def AddFactors(No):
    Sum = 0

    for i in range(1, No):
        if No % i == 0:
            Sum = Sum + i

    return Sum

def main():
    Num = int(input("Enter the number: "))

    Ans = AddFactors(Num)

    print("Addition of factors is:", Ans)

if __name__ == "__main__":
    main()