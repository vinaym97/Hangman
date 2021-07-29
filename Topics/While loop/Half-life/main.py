N = int(input())
R = int(input())
days = 0
while R <= N:
    N = N // 2
    days = days + 12
print(days)
