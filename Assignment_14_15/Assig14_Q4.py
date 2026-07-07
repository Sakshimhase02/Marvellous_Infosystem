Min = lambda No1 ,No2 : No1 if No1 < No2 else No2

def main():
    Num1 = int(input("Enter the First Number :"))
    Num2 = int(input("Enter the Second Number :"))

    Ret = min(Num1,Num2)
    print("Minimum Number iS :",Ret)

if __name__ == "__main__":
    main()