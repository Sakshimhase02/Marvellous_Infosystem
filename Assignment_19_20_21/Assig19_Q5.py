from functools import reduce

def ChkPrime(No):
    if No <= 1:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True

Multiply = lambda No: No * 2

Maximum = lambda A, B: A if A > B else B

def main():

    Data = [2, 70, 11, 10, 17, 23, 31, 77]

    print("Input List :", Data)

    FData = list(filter(ChkPrime, Data))
    print("List after filter :", FData)

    MData = list(map(Multiply, FData))
    print("List after map :", MData)

    RData = reduce(Maximum, MData)
    print("Output of reduce :", RData)

if __name__ == "__main__":
    main()