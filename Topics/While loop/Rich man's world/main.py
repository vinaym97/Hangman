year = 0
initial_sum = int(input())
while initial_sum < 700000:
    initial_sum = initial_sum * 1.071
    year = year + 1
print(year)
