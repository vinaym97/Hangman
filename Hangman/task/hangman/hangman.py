import random
list = ['python','java','kotlin','javascript']
print("H A N G M A N")
guess = random.choice(list)
remaining = guess[3:]
rest = []
for i in remaining:
    rest.append("-")
str1 = ""
string = str1.join(rest)
x = input("Guess the word " + guess[:3] + string + ":")
if x == guess:
    print("You survived!")
else:
    print("You lost!")

