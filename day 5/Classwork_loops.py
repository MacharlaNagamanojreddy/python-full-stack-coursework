#for loop
'''
s= 'python programming'
for ch in s:
    print(ch)
range(start,stop+1,step) = (0,step+1,1) by default
for i in range(8):
    print(i)
for i in range(5,96,5):
    print(i)
n = int(input("Enter a number: "))
for i in range(1,21):
    print(f"{n} x {i} = {n*i}")
'''
#break and continue
'''
for i in range(10):
    if i == 15:
            break
    print(i)
else:
    print("End of loop")
'''
pin = 1234
for i in range(5):
    user_pin = int(input("Enter your pin: "))
    if user_pin == pin:
        print("Access granted")
        break
    else:
        print("Incorrect pin")
else:
    print("dengey ra puka ")
