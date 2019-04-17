def user_input():
    one = input("1st String: \n")
    two = input("2nd String: \n")
    return one + "," + two

def print_strings(array):
    one = array[0]
    two = array[1]
    string = ""
    for x in range(min(len(one), len(two))):
        if one[x].lower() == two[x].lower():
            string += one[x]
        else:
            string += "."
    string += "." * (max(len(one), len(two)) - min(len(one), len(two)))
    print(string)

def main():
    strings = user_input().split(",")
    print_strings(strings)

if __name__ == "__main__":
    main()
