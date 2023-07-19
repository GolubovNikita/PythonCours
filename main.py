from collections import Counter

matrix = [
    [1, 2, 44],
    [22, 0, 3],
    [55, 55, 0],
]
count = 0
count2 = 0

print('1 test:')

for i in matrix:
    if 0 not in i:
        count += 1
print(count)

matrix2 = []
for i in matrix:
    for j in range(len(matrix)):
        matrix2.append(i[j])

print(matrix2)
count = Counter(matrix2)
max_value = max(count, key=lambda a: count[a])
print(count)
print(max_value)

print('3 test:')

for i in matrix:
    if 0 in i:
        count2 += 1
print(count2)
print('--------------------------')

list = []
new_list = []
for i in matrix:
    b = Counter(i)
    for j in b:
        list.append(b[j])
    new_list.append(max(list))
max_val = max(new_list)
for i in range(len(new_list)):
    if new_list[i] == max_val:
        print('First row with longest repeated queue: ', i)
        break
