def user_input():
    one = input("1st String: \n")
    two = input("2nd String: \n")
    return one + "," + two

def print_strings(array):
    one = array[0]
    two = array[1]
    string = ""
    num = min(len(one), len(two))
    i = 0
    while(i < num):
        if one[i].lower() == two[i].lower():
            string += one[i]
        else:
            string += "."
        i += 1
    string += "." * (max(len(one), len(two)) - min(len(one), len(two)))
    print(string)

def main():
    strings = user_input().split(",")
    print_strings(strings)

if __name__ == "__main__":
    main()
