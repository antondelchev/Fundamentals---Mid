treasure_chest_contents = input().split("|")

command = input()

while not command == "Yohoho!":
    data = command.split(" ")
    order = data[0]

    if order == "Loot":
        for index in range(1, len(data)):
            if data[index] not in treasure_chest_contents:
                treasure_chest_contents.insert(0, data[index])

    elif order == "Drop":
        index = int(data[1])

        if 0 <= index < len(treasure_chest_contents):
            treasure_chest_contents.append(treasure_chest_contents.pop(index))

    elif order == "Steal":
        num_of_items = int(data[1])
        stolen_items = []

        if treasure_chest_contents:
            if num_of_items <= len(treasure_chest_contents):
                for _ in range(num_of_items):
                    stolen_items.insert(0, treasure_chest_contents.pop())
            else:
                while treasure_chest_contents:
                    stolen_items.insert(0, treasure_chest_contents.pop())
                treasure_chest_contents.clear()

            print(", ".join(stolen_items))

    command = input()

if treasure_chest_contents:
    average_gain = len("".join(treasure_chest_contents)) / len(treasure_chest_contents)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
