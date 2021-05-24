items = input().split("!")
command = input()

while not command == "Go Shopping!":
    command = command.split()
    if "Urgent" in command:
        if command[1] not in items:
            items.insert(0, command[1])
    elif "Unnecessary" in command:
        if command[1] in items:
            items.remove(command[1])
    elif "Correct" in command:
        if command[1] in items:
            for index, el in enumerate(items):
                if el == command[1]:
                    items[index] = command[2]
    elif "Rearrange" in command:
        if command[1] in items:
            item = command[1]
            [items.remove(el) for el in items if el == command[1]]
            items.append(item)
    command = input()

print(", ".join(items))
