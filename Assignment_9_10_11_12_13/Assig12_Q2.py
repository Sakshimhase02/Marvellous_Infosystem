def main():
    Num = int(input("Enter the number:"))
    print("Factors are:",end=" ")  #emd=" " ...use for not go to the next line

    for i in range(1,Num+1):
        if Num % i == 0:   # check i is factors of num
            print(i,end=" ")  #print factors in single line 

if __name__ == "__main__":
    main()