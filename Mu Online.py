dungeon_rooms = input().split("|")
health = 100
bitcoins = 0

for _ in range(len(dungeon_rooms)):
    room = dungeon_rooms[_].split(" ")
    text = room[0]
    numbers = int(room[1])

    if text == "potion":
        if health + numbers <= 100:
            health += numbers
            print(f"You healed for {numbers} hp.")
            print(f"Current health: {health} hp.")
        else:
            healed = 100 - health
            health = 100
            print(f"You healed for {healed} hp.")
            print(f"Current health: {health} hp.")
    elif text == "chest":
        bitcoins += numbers
        print(f"You found {numbers} bitcoins.")
    else:
        health -= numbers
        if health > 0:
            print(f"You slayed {text}.")
        else:
            print(f"You died! Killed by {text}.")
            print(f"Best room: {_ + 1}")
            break

if health > 0:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
