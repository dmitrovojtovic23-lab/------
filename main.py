tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)
tuple3 = (5, 6, 7, 8, 9)
#Завдання 1
common = []
for item in tuple1:
    if item in tuple2 and item in tuple3:
        common.append(item)
print(common)
#Завдання 2
def get_unique(target, other1, other2):
    unique = []
    for item in target:
        if item not in other1 and item not in other2:
            unique.append(item)
    return unique
print("Унікальні для 1:", get_unique(tuple1, tuple2, tuple3))
print("Унікальні для 2:", get_unique(tuple2, tuple1, tuple3))
print("Унікальні для 3:", get_unique(tuple3, tuple1, tuple2))
#Завдання 3
same_pos = []
min_len = min(len(tuple1), len(tuple2), len(tuple3))
for i in range(min_len):
    if tuple1[i] == tuple2[i] == tuple3[i]:
        same_pos.append(tuple1[i])
print("Завдання 3 (на одній позиції):", same_pos)