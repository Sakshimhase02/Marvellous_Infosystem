from functools import reduce

Addition = lambda No1, No2: No1 + No2

def main():

    Data = [12,45,35,6,78,78]

    print("Input data is :",Data)

    Rdata = reduce(Addition , Data)

    print("Addition of data is :",Rdata)

if __name__ == "__main__":
    main()