from multiprocessing import Pool

def ChkPrime(No):

    if No <= 1:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True


def PrimeCount(No):

    Count = 0

    for i in range(1, No + 1):
        if ChkPrime(i):
            Count = Count + 1

    return Count


def main():

    Data = [10000, 20000, 30000, 40000]

    p = Pool()

    Result = p.map(PrimeCount, Data)

    p.close()
    p.join()

    for i in range(len(Data)):
        print("Prime numbers between 1 and", Data[i], "=", Result[i])


if __name__ == "__main__":
    main()