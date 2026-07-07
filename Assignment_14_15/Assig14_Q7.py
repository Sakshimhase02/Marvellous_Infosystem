Div5 = lambda No : (No % 5 == 0)

def main():
    Num = int(input("Enter the Number is :"))
    Ret = Div5(Num)
    print("Enter the Number is Div5 :",Ret)

if __name__ == "__main__":
    main()