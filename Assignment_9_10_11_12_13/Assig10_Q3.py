def main():
    Num = int(input("Enter the :"))
    Fact = 1

    for i in range(1,Num + 1):
        Fact = Fact* i

    print("Factorial of number is:",Fact)
        

if __name__ == "__main__":
    main()