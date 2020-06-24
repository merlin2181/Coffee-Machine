income = int(input())
if income < 15528:
    print("The tax for {} is {}%. That is {} dollars!".format(income, "0", "0"))
elif income < 42708:
    print("The tax for {} is {}%. That is {} dollars!".format(income, "15", round(income * 0.15)))
elif income < 132407:
    print("The tax for {} is {}%. That is {} dollars!".format(income, "25", round(income * 0.25)))
else:
    print("The tax for {} is {}%. That is {} dollars!".format(income, "28", round(income * 0.28)))