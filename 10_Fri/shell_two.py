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
    i = 0
    input = input.replace(" ","")
    
    while i < len(input):
        if input[i] in dictionary.keys() and dictionary[input[i]] != 0:
            dictionary[input[i]] -= 1
        else:
            bool = False
            break
        i += 1
    return bool

def main():
    dictionary = magazine_build()
    user = input("Ransom Note:\n")
    print(ransom_note(dictionary, user))


if __name__ == "__main__":
    main()
