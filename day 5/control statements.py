# ============================================
# LOOPS IN PYTHON - Simple & Easy Version
# ============================================

# --------------------------------------------
# PRINT 1 TO 5 (Both Loops)
# --------------------------------------------

# FOR loop - counts automatically
for i in range(1, 6):
    print(i)

# WHILE loop - runs until condition is false
i = 1 
while i <= 5:
    print(i)
    i += 1   # same as i = i + 1


# --------------------------------------------
# PRINT 1 TO ANY NUMBER (User Input)
# --------------------------------------------

# FOR loop
N = int(input("Enter a number: "))
for i in range(1, N + 1):
    print(i)

# WHILE loop
i = 1
while i <= N:
    print(i)
    i += 1


# --------------------------------------------
# PRINT EVEN NUMBERS 1 TO N
# --------------------------------------------

# FOR loop
N = int(input("Enter a number: "))
for i in range(2, N + 1, 2):
    print(i)

# WHILE loop
i = 2
while i <= N:
    print(i)
    i += 2


# --------------------------------------------
# PRINT ODD NUMBERS 1 TO N
# --------------------------------------------

# FOR loop
N = int(input("Enter a number: "))
for i in range(1, N + 1, 2):
    print(i)

# WHILE loop
i = 1
while i <= N:
    print(i)
    i += 2


# --------------------------------------------
# SUM OF N NUMBERS
# --------------------------------------------
# Adds: 1 + 2 + 3 + ... + N

def calculate_sum(N):
    total = 0                    # Start with 0
    for i in range(1, N + 1):
        total += i               # Add each number
    return total


# --------------------------------------------
# SUM OF N EVEN NUMBERS
# --------------------------------------------
# Adds: 2 + 4 + 6 + ... (first N even numbers)

def calculate_even_sum(N):
    total = 0
    for i in range(2, N * 2 + 1, 2):  # Start at 2, step by 2
        total += i
    return total


# --------------------------------------------
# MAIN FUNCTION - Run the program
# --------------------------------------------
def main():
    N = int(input("Enter a number:"))
    print("The sum of first", N, "numbers is:", calculate_sum(N))
    print("The sum of first", N, "even numbers is:", calculate_even_sum(N))

if __name__ == "__main__":    
    main()

