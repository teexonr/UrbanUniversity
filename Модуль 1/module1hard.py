# Словари и множества

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = sorted(students)
res_dict = {}

for k, v in zip(students, grades):
    res_dict[k] = sum(v) / len(v)
    
print(res_dict)
