# def main():
#     Num = int(input("Enter the Number: "))

#     Binary = ""   #create empty store binary  digit

#     while Num > 0:
#         Remainder = Num % 2   #find those number have remainder 0 
#         Binary = str(Remainder) + Binary   #convert remainder in string
#         Num = Num // 2      #divide num by 2 and keeps only int part

#     print("Binary equivalent is:", Binary)

# if __name__ == "__main__":
#     main()


#OR

def main():
    Num = int(input("Enter the Number: "))

    Binary = bin(Num)[2:]

    print("Binary equivalent is:", Binary)

if __name__ == "__main__":
    main()