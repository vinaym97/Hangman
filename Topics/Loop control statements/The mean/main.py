"""Calculate the arithmetic mean of integer numbers and output it. You will receive the integers on separate lines. The numeric sequence ends with a period ., so stop reading the input on it.
Don't round your result before outputting it.
The input will always have at least one number."""


list_ = []
while True:
    number = input()
    if number == ".":
        break
    list_.append(number)
integer_ = [int(x) for x in list_]
n = len(integer_)
total = 0
for i in integer_:
    total = total + i
print(total / n)