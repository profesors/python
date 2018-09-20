# -*- coding: utf-8 -*-

lista = [1, 7, 8, 2, 5, 6]

print len(lista)

suma = lista[0]

for contador in range(1, len(lista)):
    suma = suma + lista[contador]

print "La suma es",suma
print "La media es",float(suma)/len(lista)
