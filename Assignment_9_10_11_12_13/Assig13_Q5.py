def main():
    Mark = int(input("Enter the marks :"))

    if Mark >= 75 :
        print("Student is Distinction")

    elif Mark >= 60:
        print("Student is First class")

    elif Mark >= 50:
        print("Student is Second class")

    else:
        Mark < 50
        print("Student is FAIL")


if __name__ == "__main__":
    main()