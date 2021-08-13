vowels = ['a', 'e', 'i', 'o', 'u']
x = str(input())
for i in x:    
    if i in vowels:
        print("vowel")
    elif not i.isalpha():
        break
    else:
        print("consonant")
