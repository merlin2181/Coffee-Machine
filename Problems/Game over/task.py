scores = input().split()
# put your python code here
wrong = 0
correct = 0
for score in scores:
    if score == 'C':
        correct += 1
        continue
    if score == 'I':
        wrong += 1
        if wrong == 3:
            print("Game over")
            print(correct)
            break
else:
    print("You won")
    print(correct)