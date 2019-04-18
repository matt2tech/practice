def user_input():
    one = input("1st Integer: \n")
    two = input("2nd Integer: \n")
    return one + "," + two

def time_table(array):
    one = int(array[0])
    two = int(array[1])
    string = ""
    for x in range(two + 1):
        string += "{} * {} = {}\n".format(one, x, one * x)
    print(string)

def main():
    nums = user_input().split(",")
    time_table(nums)

if __name__ == "__main__":
    main()
