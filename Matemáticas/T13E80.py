import random

intentos = 1000000.0
aciertos = 0

for contador in range(1, int(intentos)+1):
	bolsa = ["f","f","f","f","f","f","f","f","m","m","m","m","l","l","l","l","l","l"]

	x = random.choice(bolsa)
	bolsa.remove(x)

	y = random.choice(bolsa)
	bolsa.remove(y)

	if (y != "f"):
		aciertos = aciertos + 1

	print "Intentos: ",contador,"       Probabilidad: ",aciertos/intentos
