lowest = float(input())
while True:
    num = input()
    if num == ".":
        print(lowest)
        break
    if lowest > float(num):
        lowest = float(num)