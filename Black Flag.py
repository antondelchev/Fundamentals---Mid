days_total = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

total_plunder = 0.00

for day in range(1, days_total + 1):
    total_plunder += daily_plunder
    if day % 3 == 0 and day % 5 == 0:
        total_plunder += daily_plunder * 0.5
        total_plunder -= total_plunder * 0.3
    elif day % 3 == 0:
        total_plunder += daily_plunder * 0.5
    elif day % 5 == 0:
        total_plunder -= total_plunder * 0.3

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    percentage = total_plunder / expected_plunder * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")
