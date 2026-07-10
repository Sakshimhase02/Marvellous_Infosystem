import threading

def ChkPrime(No):
    if No <= 1:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True


def Prime(Data):
    print("Prime numbers are:")

    for No in Data:
        if ChkPrime(No):
            print(No)


def NonPrime(Data):
    print("Non-prime numbers are:")

    for No in Data:
        if not ChkPrime(No):
            print(No)


def main():

    Size = int(input("Enter number of elements: "))

    Data = []

    print("Enter the elements:")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    T1 = threading.Thread(target=Prime, args=(Data,), name="Prime")
    T2 = threading.Thread(target=NonPrime, args=(Data,), name="NonPrime")

    T1.start()
    T2.start()

    T1.join()
    T2.join()


if __name__ == "__main__":
    main()