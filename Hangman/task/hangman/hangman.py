import random
list = ['python','java','kotlin','javascript']
print("H A N G M A N")
guess = random.choice(list)
# remaining = guess[3:]
# rest = []
# for i in remaining:
#     rest.append("-")
# str1 = ""
# string = str1.join(rest)
# x = input("Guess the word " + guess[:3] + string + ":")
new_list="_" * len(guess)
new_list = list()
# for _ in guess:
#     new_list = new_list + "_"
# for i in range(len(guess)):
while count < 8:
    print(new_list)
    x = input("input a letter:")
    for i in new_list:
        if x in set(guess):
            new_list[x].replace("_",x)
    else:
        print("That letter doesn't appear in the word")
    count = count + 1
# for i in guess:
#     if x in set(guess):
#         for j in guess:
#             if j == i:
#                 print(i)
#             else:
#                 print("_")
# else:
#     print("You lost!")

