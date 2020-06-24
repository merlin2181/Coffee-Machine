cafe_list = []
# Add all user input into a list until the user types 'MEOW'
while True:
    user_string = input()
    if user_string == "MEOW":
        break
    cafe_list.append(user_string.split())

base_comp = cafe_list[0]  # sets the first cafe to use as comparison

# goes through the cafe_list to find the largest number of cats
for i in range(1, len(cafe_list)):
    if int(base_comp[1]) < int(cafe_list[i][1]):
        base_comp = cafe_list[i]

print(base_comp[0])
