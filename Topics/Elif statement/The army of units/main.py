x = int(input())
if x < 1:
    print("no army")
elif x <= 9:
    print("few")
elif x <= 49:
    print("pack")
elif x <= 499:
    print("horde")
elif x <= 999:
    print("swarm")
elif x >= 1000:
    print("legion")
