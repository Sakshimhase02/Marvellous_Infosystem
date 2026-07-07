checkEven  = lambda No : No % 2 == 0

def main():

    Data = [10,2,445,67,89,345,87,88,976]
    print("Input data is :" ,Data)

    Ffilter = list(filter(checkEven , Data))
    print("Even Number are :",Ffilter)

if __name__ == "__main__":
    main()
 