def streaks(list):
    tuple = None
    temp = [0,0]
    for i in list:
        if tuple == None:
            tuple = (i, 1)
        elif i != temp[0] and temp[1] > tuple[1]:
            tuple = (temp[0], temp[1])
            temp = [i, 1]
        elif i == temp[0]:
            temp[1] += 1
        else:
            temp = [i, 1]
    if tuple != None and temp[1] > tuple[1]:
        print((temp[0], temp[1]))
    else:
        print(tuple)

def main():
    list = [1,2,11,1,1,2,2,2,2,1]
    streaks(list)

if __name__ == "__main__":
    main()
