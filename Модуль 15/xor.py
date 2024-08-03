import numpy as np
from sklearn.neural_network import MLPClassifier


def learn_xor(layers, epochs):
    # Данные для обучения (XOR)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 1, 1, 0])  # Операция XOR

    # Создание и обучение MLP-классификатора (5 000 эпох)
    mlp = MLPClassifier(hidden_layer_sizes=(layers,), activation='relu', max_iter=epochs, solver='adam')
    mlp.fit(X, y)

    # Тестирование
    return all(mlp.predict([xi])[0] == yi for xi, yi in zip(X, y))


# bad
PARAMS = ((5, 5_000), (5, 10_000), (5, 10_000), (5, 50_000))
ITER = 10
RESULT = [0] * len(PARAMS)

for _ in range(ITER):
    for i in range(len(RESULT)):
        RESULT[i] += learn_xor(*PARAMS[i])

for result, params in zip(RESULT, PARAMS):
    print(f'Верных ответов: {result}/{ITER}. Слоёв: {params[0]}. Эпох: {params[1]}.')

# good
PARAMS = ((5, 10_000), (10, 10_000), (20, 10_000), (50, 10_000))
ITER = 10
RESULT = [0] * len(PARAMS)

for _ in range(ITER):
    for i in range(len(RESULT)):
        RESULT[i] += learn_xor(*PARAMS[i])

for result, params in zip(RESULT, PARAMS):
    print(f'Верных ответов: {result}/{ITER}. Слоёв: {params[0]}. Эпох: {params[1]}.')
