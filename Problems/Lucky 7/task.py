n_values = int(input())
for _number in range(n_values):  # we use _number because we don't use that variable in the code of the for loop
    num = int(input())
    if num % 7 == 0:
        print(num * num)
