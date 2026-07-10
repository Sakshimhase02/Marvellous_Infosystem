def DisplayFactors(No):
    for i in range(1, No):
        if No % i == 0:
            print(i, end=" ")

def main():
    Num = int(input("Enter the number: "))

    print("Factors are:")
    DisplayFactors(Num)

if __name__ == "__main__":
    main()