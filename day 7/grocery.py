# Simple Grocery Billing Program for Beginners
# Run it, add items like 'milk', quantities, pay, get change!
# i need in index mode so i can select the item by index and then add the quantity and then the program will calculate the total bill and then i can pay and get change
# so that i can add the index number of the item and then add the quantity and then the program will calculate the total bill and then i can pay and get change

grocery_items = {
    "milk": 15,
    "bread": 20,
    "eggs": 50,
    "fruits": 30,
    "vegetables": 25
}
print("Welcome to the Grocery Store!")
print("Available items:")
for index, item in enumerate(grocery_items):
    print(f"{index}: {item} - ${grocery_items[item]}")
total_bill = 0
while True:
    item_index = input("Enter the index of the item you want to buy (or 'done' to finish): ")
    if item_index.lower() == "done":
        break
    if not item_index.isdigit() or int(item_index) not in range(len(grocery_items)):
        print("Invalid index. Please try again.")
        continue
    item_index = int(item_index)
    item_name = list(grocery_items.keys())[item_index]
    item_price = grocery_items[item_name]
    quantity = input(f"Enter the quantity of {item_name} you want to buy: ")
    if not quantity.isdigit() or int(quantity) <= 0:
        print("Invalid quantity. Please try again.")
        continue
    quantity = int(quantity)
    total_bill += item_price * quantity
    print(f"Added {quantity} x {item_name} to your bill. Current total: ${total_bill}")
print(f"Your total bill is: ${total_bill}")
while True:
    payment = input("Enter your payment amount: ")
    if not payment.isdigit() or int(payment) < total_bill:
        print("Insufficient payment. Please try again.")
        continue
    payment = int(payment)
    change = payment - total_bill
    print(f"Payment accepted. Your change is: ${change}")
    print("Thank you for shopping with us!")
    break
