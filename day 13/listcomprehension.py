'''a = []
for i in range(1,100):
    if i%2==0:
        a.append(i)
print(a)

l=[i for i in range(1,100) if i%2==0]
print(l)'''
'''
l=[2,3,4,6,4,8,4,79,37,2,6,7]

rl = [0 if i%2==0 else i for i in l]
print(rl)'''

l=[2,3,4,6,4,8,4,79,37,2,6,7]

rl = {i: l.count(i) for i in l}
print(rl)