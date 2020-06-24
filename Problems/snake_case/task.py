word = input()
new_word = ""
for char in word:
    if char.islower():
        new_word += char
    elif char.isupper():
        substring = "_" + char.lower()
        new_word += substring
print(new_word)