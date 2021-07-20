x = float(input())
y = float(input())
if (x == 0 and y == 0):
    print("It's the origin!")
# elif (x == 0 and y == ((-10 <= y < 0) or (0 < y <= 10))) or (x==((-10 <= x < 0) or (0 < x <= 10)) and y == 0 ): 
elif (x > 0) and (y > 0):
    print("I")
# elif (x < 0) and (y > 0):
elif x < 0 < y:
    print("II")
elif (x < 0) and (y < 0):
    print("III")
# elif (x > 0) and (y < 0):
elif y < 0 < x:
    print("IV")
else:
    print("One of the coordinates is equal to zero!")
