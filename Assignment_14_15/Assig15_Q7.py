CheckLength = lambda Str: len(Str) > 5

def main():

    Data = ["Python", "Java", "Marvellous", "C", "Programming", "AI"]

    print("Input Data :", Data)

    FData = list(filter(CheckLength, Data))

    print("Strings having length greater than 5 :", FData)

if __name__ == "__main__":
    main()