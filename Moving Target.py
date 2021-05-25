targets = list(map(int, input().split(" ")))
command = input()

while not command == "End":
    command = command.split(" ")
    index = int(command[1])
    info = int(command[2])

    if command[0] == "Shoot":
        if 0 <= index <= len(targets) - 1:
            targets[index] -= info
            if targets[index] <= 0:
                targets.pop(index)
    elif command[0] == "Add":
        if 0 <= index <= len(targets) - 1:
            targets.insert(index, info)
        else:
            print("Invalid placement!")
    elif command[0] == "Strike":
        start_index = index - info
        end_index = index + info
        if start_index >= 0 and end_index <= len(targets) - 1:
            del targets[start_index: end_index + 1]
        else:
            print("Strike missed!")

    command = input()

targets = list(map(str, targets))
print("|".join(targets))
