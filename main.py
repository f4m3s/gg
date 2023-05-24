import random
answer = input('Введите число от 1 до 6')
random_number = random.randint(1, 6)
if answer != random_number:
    print('ты выжил сосунок')
else:
    print('ты умер АХХАХАХАХАХ')
print(f'Пуля была под номером: {random_number}')
