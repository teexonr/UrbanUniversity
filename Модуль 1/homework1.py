# Строки и индексация строк

example = 'Топинамбур'

print(example[0])
print(example[-1])
print(example[int(len(example)/2):])
print(example[::-1])
print(*[example[i] for i in range(len(example)) if i % 2], sep='')
