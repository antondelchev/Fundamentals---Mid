targets = list(map(int, input().split(" ")))
command = input()
shot_targets = 0

while not command == "End":
    command = int(command)
    if command < len(targets):
        power = targets[command]
        targets[command] = -1
        for index, el in enumerate(targets):
            if el > power:
                if not el == -1:
                    targets[index] -= power
            elif el <= power:
                if not el == -1:
                    targets[index] += power
        shot_targets += 1
    command = input()

targets = list(map(str, targets))

print(f"Shot targets: {shot_targets} -> ", end="")
[print(f"{el}", end=" ") for el in targets]
