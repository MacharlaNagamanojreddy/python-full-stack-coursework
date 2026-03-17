# Simplified Python Dictionary Demo
# Original was verbose REPL session; now clean script with sections and targeted prints.

print('=== 1. Basic Dictionary Operations ===')
data = {'name': 'John', 'age': 30, 'course': 'Python', 'skills': 'python'}
print('Initial data:', data)

print('\\nAccess examples:')
print('Name:', data['name'])
print('Age:', data['age'])

data['name'] = 'Jane'
data['skills'] = 'python, java'
data['country'] = 'USA'
print('\\nAfter updates:', data)

print('=== 2. Nested List in Dictionary ===')
data['skills'] = data['skills'].split(', ')
data['skills'].append('C++')
print('With nested skills list:', data)

print('=== 3. Dictionary with Various Key Types ===')
d = dict()
d[1] = 'integer'
d[1.1] = 'floating point'
d['ygdkw'] = 'string'
d[True] = 'bool'
d[2+2j] = 'complex'
d['age'] = 31
d['Name'] = 'kushal'
print('\\nDict with mixed keys:', d)

print('=== 4. Common Dictionary Methods ===')
print('Items:', list(d.items()))
print('Keys:', list(d.keys()))
print('Values:', list(d.values()))
print('Length:', len(d))
print('Sorted keys:', sorted(d).keys())


