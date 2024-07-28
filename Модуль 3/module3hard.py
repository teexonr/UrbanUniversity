def calculate_structure_sum(*args) -> int:
    sm = 0
    for elem_data in args[0]:
        if isinstance(elem_data, list):
            sm += calculate_structure_sum(elem_data)

        elif isinstance(elem_data, dict):
            sm += calculate_structure_sum(elem_data.keys())
            sm += calculate_structure_sum(elem_data.values())

        elif isinstance(elem_data, tuple):
            sm += calculate_structure_sum(elem_data)

        elif isinstance(elem_data, set):
            sm += calculate_structure_sum(elem_data)

        else:
            if isinstance(elem_data, str):
                sm += len(elem_data)
            else:
                sm += elem_data
    return sm


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
