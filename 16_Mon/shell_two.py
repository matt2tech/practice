directions = {
    "n": 1,
    "s": -1,
    "w": 1,
    "e": -1
}

def walk(path):
    x = 0
    y = 0
    i = 0

    while i < len(path):
        if path[i] is "n" or path[i] is "s":
            y += directions[path[i]]
        else:
            x += directions[path[i]]
        i += 1

    print((x + y) == 0)

def main():
    path = ["n", "e", "s", "w", "n", "e", "s", "w", "n", "s"]
    if len(path) >= 10:
        walk(path)
    else:
        print(False)
    

if __name__ == "__main__":
    main()
