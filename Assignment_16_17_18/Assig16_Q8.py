def Display(No):
    for i in range(No):
        print("*", end=" ")

def main():
    Num = int(input("Enter the number: "))

    Display(Num)

if __name__ == "__main__":
    main()