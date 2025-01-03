import math
from random import random

rand=math.floor((random())*10)


x =input('enter a value')
if(x>10):
    print()
if(x<rand):
    print('Number is too low')
elif(x>rand):
    print('Ooops number is too huge')
else:
    print('Congratulations you got the number')

# trial = 1
# while trial<=3:
#    newX= x.isdigit()
#    if not newX
# if(x>10):
#     print('Number is not in range')
#     input('enter a number in the range')
#     trial +=trial
# elif()

    
