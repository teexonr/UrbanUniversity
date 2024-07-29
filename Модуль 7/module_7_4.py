team1_num, team2_num = 5, 6
score1, score2 = 40, 42
team1_time, team2_time = 1552.512, 2153.31451

if score1 > score2 or (score1 == score2 and team1_time < team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score1 < score2 or (score1 == score2 and team1_time > team2_time):
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

print('В команде Мастера кода участников: %d!' % team1_num)
print('Итого сегодня в командах участников: %d и %d!' % (team1_num, team2_num))
print('Команда Волшебники данных решила задач: {}!'.format(score2))
print('Волшебники данных решили задачи за {} с!'.format(team1_time))
print(f'Команды решили {score1} и {score2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {score1 + score2} задач, '
      f'в среднем по {round((team1_time + team2_time) / (score1 + score2), 2)} секунды на задачу!')
