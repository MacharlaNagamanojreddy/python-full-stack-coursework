# Age as integer
age = int(input("Enter age: "))
print(age)
age_list = list(map(int, input("Enter ages (space separated): ").split()))
print(age_list)

# Price as float
price = float(input("Enter price: "))
print(price)
price_list = list(map(float, input("Enter prices (space separated): ").split()))
print(price_list)

# Name as string
name = input("Enter name: ")
print(name)
names_tuple = tuple(input("Enter names (space separated): ").split())
print(names_tuple)

# Set with numbers
numbers_set = set(map(int, input("Enter numbers for set (space separated): ").split()))
print(numbers_set)

# Map multiple numbers (float)
numbers_float = list(map(float, input("Enter float numbers (space separated): ").split()))
print(numbers_float)

# Dictionary with names and numbers (using eval)
numbers_dict = eval(input("Enter a dictionary of numbers (e.g. {'manoj': 1, 'bhuvan': 2, 'kushal': 3}): "))
print(numbers_dict)

print("All conversions done successfully!")