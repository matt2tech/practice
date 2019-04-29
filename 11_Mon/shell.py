def split_bill(food, allergy, pay):
    total = 0

    for i in food:
        if i != food[int(allergy)]:
            total += i
        else: 
            continue

    print("\nGive back:\n{}".format(int(pay) - (total / 2)))

def main():
    food = [18.50, 9.50, 11.75, 3.00, 3.00]
    allergy = input("{}\nFood not paying for? (0-9)\n".format(food))
    pay = input("\nHow much money did you give?\n")
    split_bill(food, allergy, pay)


if __name__ == "__main__":
    main()
