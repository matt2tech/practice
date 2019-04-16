def user_input():
    while True:
        number = input("Number: ")
        if number.isdigit() and int(number) > 0:
            return int(number)
        else:
           continue

def factor(n):
    print("\n".join(["{}: is a factor of {}".format(i, n) if n % i == 0 else "{}: is not a factor of {}".format(i, n) for i in range(1,n)]))

def main():
    num = user_input()
    factor(num)


if __name__ == "__main__":
    main()
