import random 
import time
 
def castDie():
 
   input('Press any key to cast the die!')
   r = list(range(1, 7))
   print('Result: ' + str(random.choice(r)))
 
 
while True:
   time.sleep(1)
   castDie()
