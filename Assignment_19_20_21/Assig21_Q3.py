import threading

Counter = 0
Lock = threading.Lock()

def Increment():

    global Counter

    for i in range(100000):
        Lock.acquire()
        Counter = Counter + 1
        Lock.release()

def main():

    T1 = threading.Thread(target=Increment, name="Thread1")
    T2 = threading.Thread(target=Increment, name="Thread2")

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Final value of Counter:", Counter)

if __name__ == "__main__":
    main()