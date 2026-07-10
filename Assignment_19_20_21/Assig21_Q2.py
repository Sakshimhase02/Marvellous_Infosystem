import threading

def Maximum(Data):
    Max = Data[0]

    for No in Data:
        if No > Max:
            Max = No

    print("Maximum number is:", Max)


def Minimum(Data):
    Min = Data[0]

    for No in Data:
        if No < Min:
            Min = No

    print("Minimum number is:", Min)


def main():

    Size = int(input("Enter number of elements: "))

    Data = []

    print("Enter the elements:")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    T1 = threading.Thread(target=Maximum, args=(Data,), name="Maximum")
    T2 = threading.Thread(target=Minimum, args=(Data,), name="Minimum")

    T1.start()
    T2.start()

    T1.join()
    T2.join()


if __name__ == "__main__":
    main()