# Super Simple Grocery Bill - For Beginners!
prices = {"milk":15, "bread":20, "eggs":6, "fruits":30, "vegetables":25}

items = []
print("Items:", list(prices))
while True:
    item = input("Item (done to stop): ").lower()
    if item == 'done': break
    qty = int(input("Quantity: "))
    if item in prices:
        cost = prices[item] * qty
        items.append(f"{item.title()} x{qty} Rs{cost}")

total = sum(int(line.split()[2][2:]) for line in items)
print("\nYour Bill:")
for i, line in enumerate(items, 1):
    print(f"{i}. {line}")
print("TOTAL: Rs", total)

paid = float(input("Paid Rs: "))
print("Change Rs", round(paid-total, 2))

