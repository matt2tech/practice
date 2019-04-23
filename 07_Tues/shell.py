from random import randint

def build():
    array = []
    for i in range(5):
        array.append(randint(0, 1))
    return array

def true_false(array):
    count = 0
    for i in array:
        if i == 1:
            count += 1
        else:
            count -= 1
    return count > 0

def main():
    array = build()
    print("{}\nAnswer is: {}".format(array, true_false(array)))


if __name__ == "__main__":
    main()
