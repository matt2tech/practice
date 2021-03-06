from random import randint

def lets_not_drown(path):
    elevation = 0
    down_below = False
    count = 0

    for i in path:
        elevation += i

        if elevation < 0 and down_below is False:
            count += 1
            down_below = True
        elif elevation >= 0 and down_below is True:
            down_below = False
        else:
            continue

    print("Array: {}\nTimes went under sea level: {}".format(path, count))


def build():
    array = []
    for i in range(5):
        array.append(randint(-2, 2))
    return array


def main():
    array = build()
    lets_not_drown(array)


if __name__ == "__main__":
    main()
