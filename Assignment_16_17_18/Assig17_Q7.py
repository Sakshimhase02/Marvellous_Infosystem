def Display(No):
    for i in range(No, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def main():
    Num = int(input("Enter the number: "))
    Display(Num)

if __name__ == "__main__":
    main()