Odd = lambda No: No % 2 != 0
def main():

    Data = [12,54,675,356,45,63,2334,76,784,554,5435,34]

    print("Input data is :",Data)

    Fdata = list(filter(Odd,Data))
    print(" Odd number are : ",Fdata)
    
if __name__ == "__main__":
    main()