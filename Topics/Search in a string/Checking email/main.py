def check_email(string):
    if (" " not in string) and ('@' in string):
        # if '@' in string:
        if '@.' not in string:
            ind = string.rfind('@')
            print("True")
            if "." in string[ind:]:
                return True
        else:
            return False
        # else:
        #         return False
    else:
        return False
x = input()
print(check_email(x))