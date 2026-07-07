Multiplication = lambda No1 ,No2 , No3 :  No1 if (No1 > No2 and No1 > No3) else (No2 if No2 > No3 else No3)

def main():
    Num1 = int(input("Enter the First Number is :"))
    Num2 = int(input("Enter the Second Number is :"))
    Num3 = int(input("Enter the Second Number is :"))

    Ret = Multiplication(Num1 , Num2 , Num3)
    print("Enter the Multiplication :",Ret)

if __name__ == "__main__":
    main()