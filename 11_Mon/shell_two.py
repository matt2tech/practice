def split_bill(food, allergy, pay):
    print(int(pay) - ((sum(food) - food[int(allergy)]) / 2))


def main():
    food = [18.50, 9.50, 11.75, 3.00, 3.00]
    allergy = input("{}\nFood not paying for? (0-9)\n".format(food))
    pay = input("\nHow much money did you give?\n")
    split_bill(food, allergy, pay)


if __name__ == "__main__":
    main()
