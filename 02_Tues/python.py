def user_input():
    while True:
        number = input("Number: ")
        if number.isdigit() and int(number) > 0:
            return int(number)
        else:
            continue

def print_num(n):
    for i in range(1,n):
        print(str(i) + ": " + factor(i, n))

def factor(x, n):
    if n % x == 0:
        return "is a factor of {}".format(n)
    else:
        return "is not a factor of {}".format(n)

def main():
    number = user_input()
    print_num(number)


if __name__ == "__main__":
    main()
