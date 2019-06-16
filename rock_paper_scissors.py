from random import randint
player = input('rock (r), paper (p) or scissors (s)?')
print(player, 'vs', end=' ')
chosen = randint(1,3)

if chosen == 1:
    computer = 'r'

elif chosen == 2:
    computer = 's'

else:
    computer = 's'

print(computer)

if player == computer:
    print('DRAW!')

elif player == 'r' and computer == 's':
    print('player wins!')

elif player == 'r' and computer == 'p':
    print('player wins!')

elif player == 'p' and computer == 'r':
    print('player wins!')

elif player == 'p' and computer == 's':
    print('player wins!')

