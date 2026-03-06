# PYTHON OPERATORS

# 1. ARITHMETIC OPERATORS - Mathematical Operations

# +   Addition       : 5 + 3 = 8
# -   Subtraction   : 5 - 3 = 2
# *   Multiplication: 5 * 3 = 15
# /   Division      : 5 / 2 = 2.5
# //  Floor Division: 5 // 2 = 2 (rounds down)
# %   Modulus       : 5 % 2 = 1 (remainder)
# **  Exponent      : 5 ** 2 = 25 (power)

a = 10
b = 3

print("1. ARITHMETIC OPERATORS")
print("-" * 30)
print(f"a = {a}, b = {b}")
print(f"a + b  = {a + b}")    # Addition
print(f"a - b  = {a - b}")    # Subtraction
print(f"a * b  = {a * b}")    # Multiplication
print(f"a / b  = {a / b}")    # Division
print(f"a // b = {a // b}")   # Floor Division
print(f"a % b  = {a % b}")    # Modulus (remainder)
print(f"a ** b = {a ** b}")   # Exponent


# 2. ASSIGNMENT OPERATORS - Assign Values to Variables

# =   Assign value
# +=  Add and assign      : x = x + 2
# -=  Subtract and assign : x = x - 2
# *=  Multiply and assign : x = x * 2
# /=  Divide and assign   : x = x / 2

print("\n2. ASSIGNMENT OPERATORS")
print("-" * 30)
x = 5
print(f"x = 5")
x += 2      # same as: x = x + 2
print(f"x += 2  → x = {x}")

x = 5
x -= 2      # same as: x = x - 2
print(f"x -= 2  → x = {x}")

x = 5
x *= 2      # same as: x = x * 2
print(f"x *= 2  → x = {x}")

x = 5
x /= 2      # same as: x = x / 2
print(f"x /= 2  → x = {x}")

# 3. COMPARISON OPERATORS - Compare Two Values (Returns True/False)

# ==  Equal to
# !=  Not equal to
# >   Greater than
# <   Less than
# >=  Greater than or equal
# <=  Less than or equal

print("\n3. COMPARISON OPERATORS")
print("-" * 30)
print(f"a = {a}, b = {b}")
print(f"a == b  → {a == b}")   # Equal to
print(f"a != b  → {a != b}")   # Not equal
print(f"a > b   → {a > b}")    # Greater than
print(f"a < b   → {a < b}")    # Less than
print(f"a >= b  → {a >= b}")   # Greater or equal
print(f"a <= b  → {a <= b}")   # Less or equal


# 4. LOGICAL OPERATORS - Combine Conditions

# and  : True if BOTH are true
# or   : True if ANY one is true
# not  : Inverts the result (True→False, False→True)

print("\n4. LOGICAL OPERATORS")
print("-" * 30)
print(f"a = {a}, b = {b}")
print(f"a > 5 and b < 5  → {a > 5 and b < 5}")   # Both true
print(f"a > 5 or b > 5   → {a > 5 or b > 5}")    # One true
print(f"not (a > 5)      → {not (a > 5)}")        # Invert


# 5. BITWISE OPERATORS - Binary Level Operations

# &   AND   : 1 if both are 1
# |   OR    : 1 if either is 1
# ^   XOR   : 1 if different
# ~   NOT   : Inverts bits
# <<  Left Shift   : Shift bits left
# >>  Right Shift  : Shift bits right

print("\n5. BITWISE OPERATORS")
print("-" * 30)
print(f"a = {a} (binary: 1010)")
print(f"b = {b} (binary: 0011)")
print(f"a & b  → {a & b}")    # AND
print(f"a | b  → {a | b}")    # OR
print(f"a ^ b  → {a ^ b}")    # XOR
print(f"~a     → {~a}")       # NOT
print(f"a << 2 → {a << 2}")   # Left shift
print(f"a >> 2 → {a >> 2}")   # Right shift

# 6. MEMBERSHIP OPERATORS - Check if Value in Sequence

# in      : True if value exists in sequence
# not in  : True if value does NOT exist

print("\n6. MEMBERSHIP OPERATORS")
print("-" * 30)

lst = [1, 2, 3, 10]
print(f"lst = {lst}")
print(f"10 in lst      → {10 in lst}")      # True
print(f"5 in lst       → {5 in lst}")       # False
print(f"5 not in lst   → {5 not in lst}")   # True

text = "Hello Python"
print(f"\ntext = '{text}'")
print(f"'Python' in text   → {'Python' in text}")
print(f"'java' in text    → {'java' in text}")


# 7. IDENTITY OPERATORS - Check if Same Object (Same Memory)

# is      : True if same object in memory
# is not  : True if different objects in memory

print("\n7. IDENTITY OPERATORS")
print("-" * 30)

x = [1, 2, 3]
y = x           # y points to SAME object as x
z = [1, 2, 3]  # z is a NEW object with same content

print(f"x = [1, 2, 3]")
print(f"y = x        → y points to same object")
print(f"z = [1, 2, 3] → z is a new list")
print(f"\nx is y     → {x is y}")    # True (same object)
print(f"x is z     → {x is z}")    # False (different object)
print(f"x is not z → {x is not z}")


# OPERATOR PRECEDENCE - Order of Operations

# 1. ()        Parentheses
# 2. **        Exponent
# 3. * / % //  Multiply, Divide, Modulus
# 4. + -       Add, Subtract
# 5. Comparisons (==, !=, <, >, etc.)
# 6. not       Logical NOT
# 7. and       Logical AND
# 8. or        Logical OR

print("\n8. OPERATOR PRECEDENCE")
print("-" * 30)
print("Order: () → ** → * / % // → + - → comparisons → not → and → or")
print("\nExample:")
result = 2 + 3 * 4
print(f"2 + 3 * 4 = {result}")
print("Explanation: Multiplication happens first (3*4=12), then add 2")

