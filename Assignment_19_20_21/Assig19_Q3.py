from functools import reduce

FilterX = lambda No: No >= 70 and No <= 90

MapX = lambda No: No + 10

ReduceX = lambda A, B: A * B

def main():

    Data = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

    print("Input List :", Data)

    FData = list(filter(FilterX, Data))
    print("List after filter :", FData)

    MData = list(map(MapX, FData))
    print("List after map :", MData)

    RData = reduce(ReduceX, MData)
    print("Output of reduce :", RData)

if __name__ == "__main__":
    main()