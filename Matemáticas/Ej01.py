# Tenemos dos bolsas, primero elegimos de una bolsa al azar y luego un caramelo al azar
from random import *

intentos = 1000000
f = 0.0

for contador in range(1, intentos+1):
	bolsa = ["f","f","f","m","m","l","l","l"]

	x = choice(bolsa)
	print "Intentos",contador, "Obtenido",x, "P(f)=",f/intentos
	if x == "f":
		f = f + 1


print "P(fresa) = ",f/intentos
