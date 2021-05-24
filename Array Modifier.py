numbers = list(map(int, input().split(" ")))
command = input()

while not command == "end":
    command = command.split(" ")
    if "decrease" in command:
        numbers = [el - 1 for el in numbers]
    elif "multiply" in command:
        num_1_index = int(command[1])
        num_2_index = int(command[2])
        num_1 = int(numbers[num_1_index])
        num_2 = int(numbers[num_2_index])
        numbers[num_1_index] = num_1 * num_2
    elif "swap" in command:
        num_1_index = int(command[1])
        num_2_index = int(command[2])
        numbers[num_1_index], numbers[num_2_index] = numbers[num_2_index], numbers[num_1_index]
    command = input()

print(", ".join(list(map(str, numbers))))
