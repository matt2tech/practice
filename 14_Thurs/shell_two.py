def main():
    i = 1

    while i < 51:
        if (i % 3 + i % 5) == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print("{}".format(i))
        i += 1

if __name__ == "__main__":
    main()
