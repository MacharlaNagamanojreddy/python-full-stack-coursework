#pass by value and pass by referance
#int float str list tuple set dict
#for int
'''
def display(n):
    n=n+10
    print("Inside:",n)

n=10
display(n)
print("outside:",n)'''
#for float
'''
def display(n):
    n= n+10
    print("Inside:",n)

n=10.5
display(n)
print("outside:",n)'''


#for string
'''
def display(n):
    n=n+("gnan")
    print("Inside:",n)

n= "code"
display(n)
print("outside:",n)'''


#for list
'''
def display(n):
    n= n+[5,6]
    print("Inside:",n)

n=[1,2,3,4]
display(n)
print("outside:",n)'''

#for tuple
'''
def display(n):
    n=n+{5,6}
    print("Inside:",n)

n={1,2,3,4}
display(n)
print("outside:",n)

#for dic
def display(n):
    n+=(8,9)
    print("Inside:",n)

n=(3,4)
display(n)
print("outside:",n)
'''