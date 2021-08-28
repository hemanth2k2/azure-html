import random

number =int(raw_input("Guess a number (between 1 and 100):"))
randNumber = random.randint(1,100)
if number == randNumber:
	print"You guessed correctly!"else:
	print"You guessed wrong. The solution was "+str(randNumber);
