def pos_neg(No):
    if No > 0:
        print("Number is Positive")
        
    elif(No < 0):
        print("Number is Negetive")

    else:
        print("Number is Zero")

def main():
    Num = int(input("Enter the number :"))
    pos_neg(Num)

if __name__ =="__main__":
    main()