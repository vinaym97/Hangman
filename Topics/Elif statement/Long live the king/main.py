x = int(input())
y = int(input())
if (x == 1 and y == 8) or (x == 8 and y == 1) or (x == 8 and y == 8) or (x == 1 and y == 1):
    print("3")
elif (x == 1 and y == 7) or (x == 1 and y == 6) or (x == 1 and y == 5) or (x == 1 and y == 4) or (x == 1 and y == 3) \
or (x == 1 and y == 2) or (x == 2 and y == 1) or (x == 3 and y == 1) or (x == 4 and y == 1) or (x == 5 and y == 1) or (x == 6 and y == 1) or (x == 7 and y == 1) or \
(x == 8 and y == 2) or (x == 8 and y == 3) or (x == 8 and y == 4) or (x == 8 and y == 5) or (x == 8 and y == 6) or (x == 8 and y == 7) or \
(x == 2 and y == 8) or (x == 3 and y == 8) or (x == 4 and y == 8) or (x == 5 and y == 8) or (x == 6 and y == 8) or (x == 7 and y == 8):
    print("5")
else:
    print("8")
