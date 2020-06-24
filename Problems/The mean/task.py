count = 0
number = ""
total = 0
while True:
    number = input()
    if number == ".":
        print(total / count)
        break
    total += int(number)
    count += 1