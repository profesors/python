# -*- coding: utf-8 -*-
import os
import random

os.system('cls' if os.name == 'nt' else 'clear')
print u"Simulador de lotería"
print "---------------------"
n = int(raw_input("¿Qué número quieres jugar en el sorteo?"))
contador = 1
while contador <= 1000000:
    premiado = random.randint(0,99999)  # Modificado a petición de A.R.
    print premiado
    if premiado == n:
        print "Enhorabuena, te ha tocado la lotería. Intentos: ",contador
        break
    contador = contador + 1
