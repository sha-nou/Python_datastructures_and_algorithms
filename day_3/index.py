import math 
from random import random
#declare random number variable
randomNumber = math.floor((random()*10))
print(randomNumber)

guess = int (input('enter a number'))
# check if the guess is less than random number
if(guess < randomNumber):
    print ('number is below random number')
# checks if guess is greater than random number
elif(guess > randomNumber):
     print('Ooops ! guess is bigger than random number ')
else:
    print ('You got the random number')
 