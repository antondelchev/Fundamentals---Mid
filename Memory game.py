elements = input().strip().split(" ")
command = input()
number_of_moves = 0

while not command == "end":
    command = command.split(" ")
    index_1 = int(command[0])
    index_2 = int(command[1])
    number_of_moves += 1
    if index_1 == index_2 or len(elements) - 1 < index_1 or index_1 < 0 or len(elements) - 1 < index_2 or index_2 < 0:
        elements.insert(len(elements) // 2, f"-{number_of_moves}a")
        elements.insert(len(elements) // 2, f"-{number_of_moves}a")
        print("Invalid input! Adding additional elements to the board")
    elif elements[index_1] == elements[index_2]:
        print(f"Congrats! You have found matching elements - {elements[index_1]}!")
        if index_1 < index_2:
            elements.remove(elements[index_1])
            elements.remove(elements[index_2 - 1])
        else:
            elements.remove(elements[index_1 - 1])
            elements.remove(elements[index_2])
    else:
        print("Try again!")
    if len(elements) == 0:
        break
    command = input()

if len(elements) == 0 and not command == "end":
    print(f"You have won in {number_of_moves} turns!")
else:
    print("Sorry you lose :(")
    print(" ".join(elements))
