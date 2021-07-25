tax = int(input())
if 0 <= tax <= 15527:
    print("The tax for {} is 0%. That is 0 dollars!".format(tax))
elif 15528 <= tax <= 42707:
    percent = int(round(tax * 15 / 100))
    print("The tax for {} is 15%. That is {} dollars!".format(tax, percent))
elif 42708 <= tax <= 132406:
    percent = int(round(tax * 25 / 100))
    print("The tax for {} is 25%. That is {} dollars!".format(tax, percent))
elif tax >= 132407:
    percent = int(round(tax * 28 / 100))
    print("The tax for {} is 28%. That is {} dollars!".format(tax, percent))
