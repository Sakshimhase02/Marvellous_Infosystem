from multiprocessing import pool

def SumSquare(No):
    sum = 0

    for i in range(1,No + 1):
        sum = sum + (i * i)

    return sum

def main():

    Data = [1000000, 2000000, 3000000, 4000000]

    p = pool()

    Ans = p.map(SumSquare,Data)

    p.close()
    p.join()

    print("sqaure of data is :",Ans)

if __name__ == "__main__":
    main()
