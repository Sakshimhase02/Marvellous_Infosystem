def main():
    Num = int(input("Enter the Number:"))
    rev = 0

    while Num > 0:
        digit = Num % 10
        rev = (rev * 10)+digit
        Num = Num // 10

    print("Reverse Number is:",rev)


if __name__ == "__main__":
    main()