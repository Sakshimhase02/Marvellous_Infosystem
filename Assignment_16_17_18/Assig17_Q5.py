def ChkPrime(No):

    for i in range(2, No):
        if No % i == 0:
            return False

    return True

def main():

    Num = int(input("Enter the number: "))

    Ans = ChkPrime(Num)

    if Ans == True:
        print("It is Prime Number")
    else:
        print("It is Not Prime Number")

if __name__ == "__main__":
    main()