def main():
    Num = int(input("Enter the Number:"))
    temp = Num  #store oringinal number
    reversed = 0  #start la rev is  0
    while Num > 0:  # num is alsway greater than 0
        Digit = Num % 10   #extract the last digit 
        reversed = (reversed * 10)+Digit  #build reversed logic/no.s 
        Num = Num // 10  #remove last digit

    if temp == reversed:
        print("its Palindrome")

    else:
        print("its not palindrome")

if __name__ == "__main__":
    main()