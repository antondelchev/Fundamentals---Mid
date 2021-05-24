inventory = input().split(", ")
command = input()

while not command == "Craft!":
    command = command.split(" - ")
    if command[0] == "Collect":
        if command[1] not in inventory:
            inventory.append(command[1])
    if command[0] == "Drop":
        if command[1] in inventory:
            item = command[1]
            inventory.remove(item)
    if command[0] == "Renew":
        if command[1] in inventory:
            hold = command[1]
            index = inventory.index(hold)
            inventory.pop(index)
            inventory.append(hold)
    if command[0] == "Combine Items":
        sub = command[1].split(":")
        if sub[0] in inventory:
            index = inventory.index(sub[0])
            inventory.insert(index + 1, sub[1])

    command = input()

for el in inventory:
    if not inventory.index(el) == len(inventory) - 1:
        print(f"{el}, ", end="")
    else:
        print(el)
