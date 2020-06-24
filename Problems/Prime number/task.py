num = int(input())
if num > 2:
    for i in range(2, num):
        if num % i == 0:
            print("This number is not prime")
            break
    else:
        print("This number is prime")
elif num == 2:
    print("This number is prime")
else:
    print("This number is not prime")
