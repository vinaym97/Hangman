# import random
# list = ['python','java','kotlin','javascript']
# print("H A N G M A N")
# guess = random.choice(list)
# # remaining = guess[3:]
# # rest = []
# # for i in remaining:
# #     rest.append("-")
# # str1 = ""
# # string = str1.join(rest)
# # x = input("Guess the word " + guess[:3] + string + ":")
# new_list="_" * len(guess)
# new_list = list()
# # for _ in guess:
# #     new_list = new_list + "_"
# # for i in range(len(guess)):
# while count < 8:
#     print(new_list)
#     x = input("input a letter:")
#     for i in new_list:
#         if x in set(guess):
#             new_list[x].replace("_",x)
#     else:
#         print("That letter doesn't appear in the word")
#     count = count + 1
# # for i in guess:
# #     if x in set(guess):
# #         for j in guess:
# #             if j == i:
# #                 print(i)
# #             else:
# #                 print("_")
# # else:
# #     print("You lost!")
import random

list = ['python', 'java', 'kotlin', 'javascript']
print("H A N G M A N\n")
guess = random.choice(list)
product = []
newstring = ""
for i in guess:
    product.append("_")
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

