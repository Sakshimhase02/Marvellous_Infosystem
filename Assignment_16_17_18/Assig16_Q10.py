def Display(Name):
    return len(Name)

def main():
    Name = input("Enter your name: ")

    Ans = Display(Name)

    print("Length of name is:", Ans)

if __name__ == "__main__":
    main()