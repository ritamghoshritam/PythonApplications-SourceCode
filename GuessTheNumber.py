import random
 
n = random.randrange(1, 101)
print('I\'ve though a number between 1 and 100!')
 
while True:
    try:
        g = input('Guess!')
        g = int(g)
        if not 100 > g > 0:
            print('It\'s in between 0 and 100!')
    except ValueError:
        print('Enter an integer')
        continue
 
    if g == n:
        print('Congratulations!')
        break
 
    if g < n:
        print('Larger')
 
    if g > n:
        print('Smaller')
