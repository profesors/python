# Tenemos dos bolsas, primero elegimos de una bolsa al azar y luego un caramelo al azar
from random import *

intentos = 1000000
f = 0.0

for contador in range(1, intentos+1):
	bolsa1 = ["f","f","f","f","f","f","f","f","m","m","m","m","l","l","l","l","l","l"]
	bolsa2 = ["m","m","m","m","l","l","l","l","l","l"]

	n = randint(1, 100)
	if n <= 25:
		x = choice(bolsa1)
		if x == "f":
			f = f + 1
	else:
		x = choice(bolsa2)

print "P(fresa) = ",f/intentos
