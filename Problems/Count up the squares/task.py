# put your python code here
number = int(input())
if number == 0:
    print(number)
else:
    total = number
    total_sq = number ** 2
    while total != 0:
        number = int(input())
        total += number
        total_sq += number ** 2
    print(total_sq)