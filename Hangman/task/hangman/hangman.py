import random
list = ['python','java','kotlin','javascript']
print("H A N G M A N")
x = input("Guess the word >")
if x == random.choice(list):
    print("You survived!")
else:
    print("You lost!")

