import random
answer = input('choice number from 1 to 6')
random_number = random.randint(1, 6)
if answer != random_number:
    print('you are survive')
else:
    print('You died')
print(f'Bullet: {random_number}')
