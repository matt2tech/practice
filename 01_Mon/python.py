def user_input():
    while True:
        number = input("Number:\n")
        if number.isdigit() > 0:
            return int(number)
        else:
            continue

def print_num(n):
    for i in range(1,n):
        print(str(i) + ": " + even_or_odd(i))

def even_or_odd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"

def main():
    number = user_input()
    print_num(number)


if __name__ == "__main__":
    main()
