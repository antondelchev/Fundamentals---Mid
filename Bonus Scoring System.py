import math

num_of_students = int(input())
lectures_count = int(input())
initial_bonus = int(input())

bonus_points = 0
attended_lectures = 0

for num in range(1, num_of_students + 1):
    attended = int(input())
    current_bonus = math.ceil(attended / lectures_count * (5 + initial_bonus))
    if current_bonus >= bonus_points:
        bonus_points = current_bonus
        attended_lectures = attended

print(f"Max Bonus: {bonus_points}.")
print(f"The student has attended {attended_lectures} lectures.")
