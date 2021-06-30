pirate_ship_status = [int(el) for el in input().split(">")]
war_ship_status = [int(el) for el in input().split(">")]
max_health_of_section = int(input())

command = input()

while not command == "Retire":
    data = command.split()
    order = data[0]

    if order == "Fire":
        target_index = int(data[1])
        damage = int(data[2])

        if 0 <= target_index < len(war_ship_status):
            war_ship_status[target_index] -= damage
            if war_ship_status[target_index] <= 0:
                print("You won! The enemy ship has sunken.")
                war_ship_status.clear()
                break

    elif order == "Defend":
        start_index = int(data[1])
        end_index = int(data[2])
        damage = int(data[3])

        if 0 <= start_index < end_index < len(pirate_ship_status):
            for index in range(start_index, end_index + 1):
                pirate_ship_status[index] -= damage
                if pirate_ship_status[index] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    pirate_ship_status.clear()
                    break

    elif order == "Repair":
        index = int(data[1])
        health = int(data[2])
        if 0 <= index < len(pirate_ship_status):
            if pirate_ship_status[index] + health <= max_health_of_section:
                pirate_ship_status[index] += health
            elif pirate_ship_status[index] + health > max_health_of_section:
                pirate_ship_status[index] = max_health_of_section

    elif order == "Status":
        count = 0
        for el in pirate_ship_status:
            if el < max_health_of_section * 0.2:
                count += 1

        print(f"{count} sections need repair.")

    command = input()

if pirate_ship_status and war_ship_status:
    print(f"Pirate ship status: {sum(pirate_ship_status)}")
    print(f"Warship status: {sum(war_ship_status)}")
