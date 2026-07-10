def CountDigits(No):
    Count = 0

    while No > 0:
        Count = Count + 1
        No = No // 10

    return Count

def main():
    Num = int(input("Enter the number: "))

    Ans = CountDigits(Num)

    print("Number of digits is:", Ans)

if __name__ == "__main__":
    main()