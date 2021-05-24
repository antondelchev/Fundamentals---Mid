people_total = int(input())
state_of_lift = input().split(" ")

for index, wagon in enumerate(state_of_lift):
    wagon = int(wagon)
    free_seats = 4 - wagon
    if free_seats > people_total:
        wagon += people_total
        free_seats -= people_total
        people_total -= people_total
    else:
        people_total -= free_seats
        wagon += free_seats
        free_seats = 0

    state_of_lift[index] = str(wagon)

    if people_total < free_seats and index == len(state_of_lift) - 1:
        print("The lift has empty spots!")

if people_total > 0:
    print(f"There isn't enough space! {people_total} people in a queue!")

print(" ".join(state_of_lift))
