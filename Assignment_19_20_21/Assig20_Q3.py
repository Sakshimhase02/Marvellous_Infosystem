import threading

def EvenList(Data):
    Sum = 0

    print("Even numbers are:")

    for No in Data:
        if No % 2 == 0:
            print(No)
            Sum = Sum + No

    print("Sum of even numbers:", Sum)


def OddList(Data):
    Sum = 0

    print("Odd numbers are:")

    for No in Data:
        if No % 2 != 0:
            print(No)
            Sum = Sum + No

    print("Sum of odd numbers:", Sum)


def main():

    Size = int(input("Enter number of elements: "))

    Data = []

    print("Enter the elements:")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    T1 = threading.Thread(target=EvenList, args=(Data,), name="EvenList")
    T2 = threading.Thread(target=OddList, args=(Data,), name="OddList")

    T1.start()
    T2.start()

    T1.join()
    T2.join()


if __name__ == "__main__":
    main()