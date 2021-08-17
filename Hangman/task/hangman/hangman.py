import random

pro = ""
list = ['python', 'java', 'kotlin', 'javascript']
print("H A N G M A N\n")
guess = random.choice(list)
product = []
newstring = ""
repeat = set()
for i in guess:
    product.append("-")
count = 0
while True:
    if count == 8:
        print("You lost!")
        break
    print()
    if pro.join(product).replace(" ", "") == guess:
        print()
        print(pro.join(product).replace(" ", ""))
        print("You guessed the word!")
        print("You survived!")
        break
        if count == 8:
            break
    print(newstring.join(product))
    x = input("Input a letter:")
    if len(x) != 1:
        print("You should input a single letter")
        continue
    if x.islower() == False or x.isalpha() == False:
        print("Please enter a lowercase English letter")
        continue
    if x in repeat:
        print("You've already guessed this letter")
        continue
    if pro.join(product).replace(" ", "") != guess:
        if x in guess:
            if x in set(product):
                print("No improvements")
                if count == 8:
                    break
            else:
                count = count - 1
                for i in range(0, len(guess)):
                    if x == guess[i]:
                        #                         if x not in product:
                        product[i] = x
                        if count == 8:
                            break
        else:
            print("That letter doesn't appear in the word")
    if count == 8:
        print("You lost!")
        break
    count = count + 1

    repeat.add(x)
else:
    print("You lost!")