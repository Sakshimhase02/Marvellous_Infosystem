Even = lambda No1 : (No1 % 2 == 0)

def main():
    Num = int(input("Enter the Number :"))
    Ret = Even(Num)
    print("Even Number is :",Ret)

if __name__ == "__main__":
    main()
    