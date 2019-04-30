def user_input():
    while True:
        string = input("String: ")
        if len(string) > 0:
            return string
        else:
            continue

def user_input2():
    while True:
        number = input("Number: ")
        if number.isdigit() and int(number) > 0:
            return int(number)
        else:
            continue

def infinite_repetition(string, number):
    wholes = number // len(string)
    remainder = number % len(string)
    print(string.count("a") * wholes + string[:remainder].count("a"))

def main():
    string = user_input()
    number = user_input2()
    infinite_repetition(string, number)

if __name__ == "__main__":
    main()
