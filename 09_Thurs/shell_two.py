def matching_socks(array):
    count = 0
    i = 0

    while i < len(array):
        x = i + 1
        while x < len(array):
            if array[i] == array[x] and array[i] != None:
                count += 1
                array[i] = None
                array[x] = None
                break
            else:
                x += 1
                continue
        i += 1
    print(count)

def main():
    array = ["blue", "red", "yellow", "green", "yellow", "yellow", "yellow", "blue"]
    matching_socks(array)


if __name__ == "__main__":
    main()
