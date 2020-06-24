guest_list = []
while True:
    name = input()
    if name == ".":
        print(guest_list)
        print(len(guest_list))
        break
    guest_list.append(name)