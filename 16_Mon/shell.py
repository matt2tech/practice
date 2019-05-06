directions = {
    "n": 1,
    "s": -1,
    "w": 1,
    "e": -1
}

def walk(path):
    x = 0
    y = 0
    for i in path:
        if i is "n" or i is "s":
            y += directions[i]
        else:
            x += directions[i]

    print((x + y) == 0)

def main():
    path = ["n", "e", "s", "w", "n", "e", "s", "w", "n", "s"]
    if len(path) >= 10:
        walk(path)
    else:
        print(False)
    

if __name__ == "__main__":
    main()
