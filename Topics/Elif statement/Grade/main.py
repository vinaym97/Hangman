score = int(input())
max_score = int(input())
percent = (score / max_score) * 100
if 90 <= percent <= 100:
    print("A")
elif 80 <= percent < 90:
    print("B")
elif 70 <= percent < 80:
    print("C")
elif 60 <= percent < 70:
    print("D")
else:
    print("F")
