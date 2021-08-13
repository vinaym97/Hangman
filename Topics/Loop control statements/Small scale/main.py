float_number = []
while True:
    x = input()
    if x == ".":
        break
    float_number.append(x)
float_number = [float(x) for x in float_number] 
min_val = float_number[0]
for i in float_number:
    if i < min_val:
        min_val = i
print(min_val)
