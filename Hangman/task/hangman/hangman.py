import random
list = ['python', 'java', 'kotlin', 'javascript']
print("H A N G M A N\n")
guess = random.choice(list)
product = []
newstring = ""
for i in guess:
    product.append("-")
count = 0
while count < 8:
    print(newstring.join(product))
    x = input("Input a letter:")
    if product != guess:
        if x in guess:
            for i in range(0, len(guess)):
                if x == guess[i]:
                    product[i] = x
        else:
            print("That letter doesn't appear in the word")
    print()
    count = count + 1
else:
    print("Thanks for playing!\nWe'll see how well you did in the next stage")

