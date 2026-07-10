def check(No):
    if No % 5 == 0:
        return True

    else:
        return False

def main():
    Num = int(input("Enter the Number :"))
    Ans=check(Num)

    print(Ans) 


if __name__ =="__main__":
    main()