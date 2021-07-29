n = []
total = 0
while(1):
    x = int(input())
    if x == 55:
        print(len(n))
        print(total)
        print(round(total/len(n)))
        break
    n.append(x)
    total = total + x
    x = x + 1