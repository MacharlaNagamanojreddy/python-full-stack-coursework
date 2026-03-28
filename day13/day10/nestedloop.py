'''n = int(input("Enter the size: "))
for row in range(n):
   for col in range(n):
      print('*',end=' ')
   print()'''

'''n = int(input("Enter the size: "))
for row in range(n):
   for col in range(n):
      print(col,end=' ')
   print()
'''
'''
n = int(input("Enter size: "))
for row in range(n):
    for col in range(n):
        print((row+col)%2,end=' ')
    print()
'''
'''
n = int(input('enter number: '))
for row in range(n):
    for col in range(row+1):
        print('*',end =' ')
    print()'''
#revrse
''' 
* * * * * 
* * * *
* * *
* *
*'''
'''
n = int(input("Enter the size: "))
for row in range(n):
   for col in range(n-row):
      print('*',end=' ')
   print()'''

n = int(input("Enter the size: "))
for row in range(n):
   for spc in range(n-row-1):
      print(' ',end=' ')
   for col in range(row+1):
       print('*',end=' ')
   print()