def chkNum(No):
    if No % 2 == 0:
        print("Even Number")

    else:
        print("Odd number")
def main():
    Num =  int(input("Enter the Number :"))
    chkNum(Num)
if __name__ =="__main__":
    main()