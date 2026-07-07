from functools import reduce

Maximum = lambda No1, No2: No1 if No1 < No2 else No2

def main():
    Data = [23, 434, 5, 23, 45, 344, 56, 678]

    print("Input Data :", Data)

    RData = reduce(Maximum, Data)

    print("Maximum number is :", RData)

if __name__ == "__main__":
    main()