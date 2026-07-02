def main():
    Char =  input("enter the character :")
    
    Vowels = ["a","e","i","o","u","A","E","I","O","U"]
    
    if Char in Vowels:
        print("its Vowels")
    else:
        print("Its Consonant")


if __name__ == "__main__":
    main()