initial_amt = int(input())
yrs = 0
while initial_amt < 700000:
    initial_amt *= 1.071
    yrs += 1
print(yrs)