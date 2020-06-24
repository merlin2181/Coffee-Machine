# put your python code here
a = int(input())
b = int(input())
total = 0
count = 0
for i in range(a, (b + 1)):
    if i % 3 == 0:
        total += i
        count += 1

print(total / count)