# -*- coding: utf-8 -*-

lista = [1, 7, 8, 2, 5, 6]

suma = lista[0]

for contador in range(1, 5):
    print suma
    suma = suma + lista[contador]

print "La suma total es:", suma
