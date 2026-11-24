def checkString(s):

    current_element = ""

    for i in s:
        if i == 'a' and current_element =='b':
            return False
        else:
            current_element = i

    return True

print(checkString('aaabbb'))