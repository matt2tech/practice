def triple_up(array):
    bool = False
    for i in range(len(array)):
        if len(array) - i >= 3:
            bool = (array[i] < array[i+1] and array[i+1] < array[i+2])
            if bool == True:
                break
            else:
                continue
        else:
            bool = False
    return bool

def main():
    array = [1,2,1,2,1,2]
    if len(array) >= 3 :
        answer = triple_up(array)
    else:
        answer = False
    print(answer)
    
    
if __name__ == "__main__":
    main()
