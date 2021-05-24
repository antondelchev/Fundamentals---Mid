numbers = list(map(int, input().split(" ")))
average_num = sum(numbers) / len(numbers)
greater = []

for el in numbers:
    if el > average_num:
        greater.append(el)

greater = sorted(greater, reverse=True)
counter = 0
if len(numbers) == 1 or average_num == numbers[0]:
    print("No")
else:
    for num in greater:
        if len(numbers) >= 5:
            print(num, end=" ")
            counter += 1
            if counter == 5:
                break
        else:
            print(num, end=" ")
