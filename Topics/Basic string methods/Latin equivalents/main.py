def normalize(name):
    # new_name =
    return name.replace('ë', 'e').replace('é', 'e').replace('á', 'a').replace('å', 'a').replace('œ', 'oe').replace('æ', 'ae')
word = input()
print(normalize(word))

