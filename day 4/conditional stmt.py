# ============================================
# PYTHON CONDITIONAL STATEMENTS - SIMPLE & EASY
# ============================================

# 1. IF - Runs only when TRUE
balance = 2000
if balance > 1000:
    print("You have money!")

# 2. IF-ELSE - TRUE or FALSE (one will run)
age = 18
if age >= 18:
    print("Adult")
else:
    print("Child")

# 3. IF-ELIF-ELSE - Multiple conditions (first TRUE wins)
marks = 75
if marks >= 90:
    print("A Grade")
elif marks >= 70:
    print("B Grade")
elif marks >= 50:
    print("C Grade")
else:
    print("Fail")

# 4. NESTED IF - IF inside IF
is_logged = True
is_premium = True

if is_logged:
    if is_premium:
        print("Premium User")
    else:
        print("Free User")
else:
    print("Please Login")

# 5. AND, OR - Combine conditions
age = 25
income = 50000

if age >= 18 and income >= 30000:
    print("Eligible for loan")

# 6. MEMBERSHIP - Check in list
fruits = ["apple", "mango", "banana"]
if "orange" in fruits:
    print("Orange found")
else:
    print("Orange not found")

# 7. NOT - Reverse condition
is_raining = False
if not is_raining:
    print("Go outside")

# ============================================
# QUICK REFERENCE
# ============================================
print("\n--- CHEAT SHEET ---")
print("if      = Run if TRUE")
print("elif    = Else if next condition")
print("else    = Run if all FALSE")
print("and     = Both must be TRUE")
print("or      = Any one TRUE")
print("in      = Value in list")
print("not in  = Value NOT in list")

