first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
customers_num = int(input())
hours_count = 0

while customers_num > 0:
    customers_num -= first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
    hours_count += 1
    if hours_count % 4 == 0:
        hours_count += 1

print(f"Time needed: {hours_count}h.")
