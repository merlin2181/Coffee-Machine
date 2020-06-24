n = int(input())
r = int(input())
t = 0
while n >= r:
    t += 1
    n //= 2

print(t * 12)