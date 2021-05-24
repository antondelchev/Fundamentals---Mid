command = input().strip()

total_not_taxed = 0

while command.isdigit() or "." in command or "-" in command:
    price = float(command)
    if price <= 0:
        print("Invalid price!")
    else:
        total_not_taxed += price
    command = input().strip()

if total_not_taxed == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_not_taxed:.2f}$")
    print(f"Taxes: {total_not_taxed * 0.2:.2f}$")
    print("-----------")
    final_price = total_not_taxed + total_not_taxed * 0.2
    if command == "special":
        print(f"Total price: {final_price * 0.9:.2f}$")
    else:
        print(f"Total price: {final_price:.2f}$")
