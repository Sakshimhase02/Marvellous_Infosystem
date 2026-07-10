import threading

def Small(String):
    Count = 0

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)

    for ch in String:
        if ch.islower():
            Count = Count + 1

    print("Number of lowercase letters :", Count)


def Capital(String):
    Count = 0

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)

    for ch in String:
        if ch.isupper():
            Count = Count + 1

    print("Number of uppercase letters :", Count)


def Digits(String):
    Count = 0

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)

    for ch in String:
        if ch.isdigit():
            Count = Count + 1

    print("Number of digits :", Count)


def main():

    Str = input("Enter a string : ")

    T1 = threading.Thread(target=Small, args=(Str,), name="Small")
    T2 = threading.Thread(target=Capital, args=(Str,), name="Capital")
    T3 = threading.Thread(target=Digits, args=(Str,), name="Digits")

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()


if __name__ == "__main__":
    main()