#print all even number from 0 to num 
def main():
    Num = int(input("Enter the :"))
    for i in range(Num):
        if i % 2 == 0:
            print(i)

if __name__ == "__main__":
    main()