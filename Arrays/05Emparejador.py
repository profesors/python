# -*- coding: utf-8 -*-
# Modificar: Cambiar el tipo y la longitud de las listas
# Por ejemplo, emparejar personas, premios o depórtes favoritos
# Emparejar personas para un concurso de baile. Asignar de una tercera lista
#   un estilo musical que deberán bailar

import random

personas = ["Alberto", "Beatriz", "Carlos"]
equipos = ["Real Madrid", u"Atlético de Madrid", "Barça"]

a = random.randint(0,2)
b = random.randint(0,2)

print personas[a],"disfruta viendo al",equipos[b],"en TV"
