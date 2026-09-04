prices = []
print("Enter prices of 6 items:")
for i in range(1, 7):
    price = int(input(f"Item {i}: "))
    prices.append(price)

print()

budget = int(input("Enter total budget: "))
print()

current_total = 0
bought_items = []

for i, price in enumerate(prices, start=1):
    if current_total + price <= budget:
        current_total += price
        bought_items.append(price)
        print(f"Item {i} = {price} -> buy")
    else:
        print(f"Item {i} = {price} -> cannot buy")
    
    print(f"Current total = {current_total}")
    print()

remaining_budget = budget - current_total
print(f"Bought items: {bought_items}")
print(f"Total spent: {current_total}")
print(f"Remaining budget: {remaining_budget}")