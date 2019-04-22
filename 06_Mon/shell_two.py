from random import randint

def build():
    array = []
    for i in range(5):
        array.append(randint(1, 21))
    return array

def min_max(array):
    min = array[0]
    max = array[0]
    i = 0

    while(i < len(array)):
        if array[i] < min:
            min = array[i]
        elif array[i] > max:
            max = array[i]
        else:
            i += 1
            continue
        i += 1
    return max - min


def main():
    array = build()
    print("{}\nAnswer is: {}".format(array, min_max(array)))


if __name__ == "__main__":
    main()
