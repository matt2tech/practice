from random import randint

def build():
    array = []
    for i in range(5):
        array.append(randint(1, 21))
    return array

def min_max(array):
    min = array[0]
    max = array[0]
    for i in array:
        if i < min:
            min = i
        elif i > max:
            max = i
        else:
            continue
    return max - min


def main():
    array = build()
    print("{}\nAnswer is: {}".format(array, min_max(array)))


if __name__ == "__main__":
    main()
