CheckEven = lambda No: No % 2 == 0

def main():

    Data = [10, 15, 20, 23, 40, 55, 60]

    print("Input Data :", Data)

    FData = list(filter(CheckEven, Data))

    print("Count of Even Numbers :", len(FData))

if __name__ == "__main__":
    main()