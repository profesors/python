# -*- coding:utf-8 -*-
# Elegimos caramelos de una bolsa, calcular la probabilidad de obtener un caramelo de
#	fresa después de un número determinado de intentos
from random import *

intentos = 10000
acumulador = 0.0

for i in range(1, intentos+1):
	bolsa = ["f","f","f","m","m","l"]

	x = choice(bolsa)
	print "Intentos",i, "P(f)=",acumulador/intentos

	if x == "f":
		acumulador = acumulador + 1

print "P(fresa) = ",acumulador/intentos
