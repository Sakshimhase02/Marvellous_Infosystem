Square = lambda No: (No * No)

def main():

    Data = [2,3,4,5,6,7,8]

    print("Input Data IS : ",Data)

    Num =list(map(Square , Data))
    print("enter the Square of each number : ",Num)

if __name__ == "__main__":
    main()