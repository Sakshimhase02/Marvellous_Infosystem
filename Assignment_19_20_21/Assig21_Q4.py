import threading

Sum = 0
Product = 1

def Addition(Data):
    global Sum

    for No in Data:
        Sum = Sum + No


def Multiplication(Data):
    global Product

    for No in Data:
        Product = Product * No


def main():

    Size = int(input("Enter number of elements: "))

    Data = []

    print("Enter the elements:")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    T1 = threading.Thread(target=Addition, args=(Data,), name="Addition")
    T2 = threading.Thread(target=Multiplication, args=(Data,), name="Multiplication")

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Addition of elements:", Sum)
    print("Product of elements:", Product)


if __name__ == "__main__":
    main()