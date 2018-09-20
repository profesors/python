# -*- coding: utf-8 -*-
import os
import random

os.system('cls' if os.name == 'nt' else 'clear')
print "Simulador de combate Pokemon v0.1"
print "--------------------------------"

miVida = 10
suVida = 10
contador = 1

while contador <= 100:
    # Mi Pokemon ataca
    miAtaque = random.randint(1,10)
    if miAtaque > 5:
        suVida = suVida-random.randint(1,3)
        print u"Tú: Éxito al atacar. Vida del rival ",suVida
    else:
        print u"Tú: Fallo al atacar"

    # Mi rival me ataca
    suAtaque = random.randint(1,10)
    if suAtaque > 5:
        miVida = miVida - random.randint(1,3)
        print u"Rival: Éxito al atacar. Tu vida ",miVida
    else:
        print u"Rival: Fallo al atacar"
    print ""

    # Comprueba si he perdido el combate
    if miVida <=0:
        print "Has perdido"
        break

    # Comprueba si mi rival ha perdido el combate
    if suVida <=0:
        print "Has ganado"
        break

    contador = contador + 1
print ""
