houses = list(map(int, input().split("@")))

command = input()
current_position = 0

while not command == "Love!":
    command = command.split(" ")
    position = int(command[1]) + current_position

    if position < len(houses):
        if houses[position] > 0:
            houses[position] -= 2
            if houses[position] == 0:
                print(f"Place {position} has Valentine's day.")
        else:
            print(f"Place {position} already had Valentine's day.")
        current_position = position
    else:
        position = 0
        current_position = 0
        if houses[position] > 0:
            houses[position] -= 2
            if houses[position] == 0:
                print(f"Place {position} has Valentine's day.")
        else:
            print(f"Place {position} already had Valentine's day.")

    command = input()

print(f"Cupid's last position was {current_position}.")

counter = 0
for el in houses:
    if not el == 0:
        counter += 1

if not counter == 0:
    print(f"Cupid has failed {counter} places.")
else:
    print("Mission was successful.")
