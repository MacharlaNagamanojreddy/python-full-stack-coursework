'''
expression = input("Enter expression: ")
result = eval(expression)
print(result)
'''
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Division:", a / b)
print("Remainder:", a % b)
print("Multiplication:", a * b)
'''
'''
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b

exp = input()
if '+' in exp:
    a,b = exp.split('+')
    print(add(int(a),int(b)))

elif '-' in exp:
    a,b = exp.split('-')
    print(sub(int(a),int(b)))

elif '*' in exp:
    a,b = exp.split('*')
    print(mul(int(a),int(b)))

elif '/' in exp:
    a,b = exp.split('/')
    print(div(int(a),int(b)))

elif '%' in exp:
    a,b = exp.split('%')
    print(mod(int(a),int(b)))
'''