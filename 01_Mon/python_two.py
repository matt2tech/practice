def user_input():
    while True:
        number = input("Number: ")
        if number.isdigit() and int(number) > 0:
            return int(number)
        else:
           continue

def even_or_odd(n):
    print("\n".join(["{}: even".format(i) if i % 2 == 0 else "{}: odd".format(i) for i in range(1,n)]))

def main():
    num = user_input()
    even_or_odd(num)


if __name__ == "__main__":
    main()
