from functools import reduce

Product = lambda No1, No2: No1 * No2

def main():

    Data = [2, 3, 4, 5]

    print("Input Data :", Data)

    RData = reduce(Product, Data)

    print("Product of all elements :", RData)

if __name__ == "__main__":
    main()