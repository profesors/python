# -*- coding: utf-8 -*-
# Fuente: http://mundogeek.net/archivos/2008/04/12/sockets-en-python/
import socket

s = socket.socket()
s.connect(("localhost", 9999))

while True:
      mensaje = raw_input("> ")
      s.send(mensaje)
      if mensaje == "quit":
         break

print "adios"

s.close()
