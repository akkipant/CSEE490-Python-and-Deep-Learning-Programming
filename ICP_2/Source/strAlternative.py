def string_Alternative(Str):  # Function Definition
    #return Str[::2]     # Return alternative characters of string
    newStr = ''
    count = 0
    for x in Str:
        count += 1
        if count%2:
            newStr += x

    return newStr


if __name__ == '__main__':
    print(string_Alternative(input("Enter String : ")))     # Function call
