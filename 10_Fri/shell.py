def magazine_build():
    magazine = "Hello World".replace(" ", "")
    dictionary = {}
    for i in magazine:
        if i not in dictionary.keys():
            dictionary[i] = 1
        else:
            dictionary[i] += 1
    return dictionary

def ransom_note(dictionary, input):
    bool = True
    for i in input.replace(" ", ""):
        if i in dictionary.keys() and dictionary[i] != 0:
            dictionary[i] -= 1
        else:
            bool = False
            break
    return bool

def main():
    dictionary = magazine_build()
    user = input("Ransom Note:\n")
    print(ransom_note(dictionary, user))


if __name__ == "__main__":
    main()
