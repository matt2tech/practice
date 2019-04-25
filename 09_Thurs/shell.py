def matching_socks(array):
    count = 0

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j] and array[i] != None:
                count += 1
                array[i] = None
                array[j] = None
                break
            else:
                continue
    print(count)

def main():
    array = ["blue", "red", "yellow", "green", "yellow", "yellow", "yellow"]
    matching_socks(array)


if __name__ == "__main__":
    main()
