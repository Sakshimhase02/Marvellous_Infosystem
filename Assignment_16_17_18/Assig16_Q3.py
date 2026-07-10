def Add(No1,No2):
    return No1 + No2 

def main():
    Num1 =  int(input("Enter the Number :"))
    Num2 =  int(input("Enter the Number :"))
    Ans = Add(Num1 , Num2)
    print("Addition Of Two Number is :" , Ans)

if __name__ =="__main__":
    main()