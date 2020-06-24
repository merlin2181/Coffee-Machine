# put your python code here
word = input()
index = 0
neg_index = -1
while index < len(word):
    if word[index] == word[neg_index]:
        neg_index -= 1
        index += 1
        continue
    print("Not palindrome")
    break
else:
    print("Palindrome")