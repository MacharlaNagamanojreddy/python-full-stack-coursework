#recurstion - function calling it self
#printing 1 - 10 using recursion
'''def display(n):
    if n>10:
        return 
    print(n)
    display(n+1)

display(1)'''
#printing 10 -1 using recursion

'''
def display(n):
    if n>10:
        return 
    display(n+1)
    print("After:",n)

display(1)'''

#printing python programming 
'''    
def display(s,i):
    if i == len(s):
        return
    print(s[i])
    display(s,i+1)


display("Python Programming",0)'''

#print p 
#py 
#pyth
#......
#python programming
'''
def display(s,i):
    if i == len(s):
        return
    print(s[:i+1])
    display(s,i+1)

display("python programing",0)'''

'''
def display(s,i):
    if  i<=0:
        return
    display(s,i-1)
    print(s*i)
display("abc",5)
'''

'''
def display(s,i,n):
    if i==len(s)-n:
        return
    print(s[i:i+n])
    display(s,i+1,n)

display("abcdefgh",0,3)'''

#sum of elements using recurstions
'''
def display(l,i,sum):
    if i==len(l):
        return sum
    return display(l,i+1,sum+l[i])

print(display([1,2,3,4,5,6,7,8],0,0))

'''


#sum of string
def display(l,i,sum):
    if i ==len(l):
        return sum
    return display(l,i+1,sum+l[i])

print(display(['python','java','html','css','flask'],0,''))