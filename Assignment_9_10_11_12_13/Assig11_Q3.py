def main():
    Num = int(input("Enter the Number:"))
    sum = 0
    
    while Num > 0:
        Digit = Num % 10
        sum = sum + Digit
        Num = Num // 10
    print("Sum of the number is:",sum)

if __name__ == "__main__":
    main()

# def main():
#     sum = 0
#     for i in range(0,100):
#         print(i)
#         sum = sum + i

#     print("Sum of the number is:",sum)

# if __name__ == "__main__":
#     main()