from funciones import barajar
from funciones import desglosaCarta
from funciones import traduceBarajaEspañola
from funciones import puntosMazo
from funciones import reparteCartas
from random import randint
from random import shuffle
import re

barajaEspañola = ['1B','2B','3B','4B','5B','6B','7B','8B','9B','10B','11B','12B','1C','2C','3C','4C','5C','6C','7C','8C','9C','10C','11C','12C',
                  '1E','2E','3E','4E','5E','6E','7E','8E','9E','10E','11E','12E','10','2O','3O','4O','5O','6O','7O','8O','9O','10O','11O','12O']

cartasUsuario = reparteCartas(barajaEspañola)
puntuacion = puntosMazo(cartasUsuario)

print("#=======PUNTUACION CORRESPONDIENTE A LAS CARTAS==========#")

print("As -> 11 ptos")
print("3 -> 10ptos")
print("Rey -> 4 ptos")
print("Caballo -> 3 ptos")
print("Sota -> 2 ptos")

print("#========================================================#")
print("Tus Cartas Son: ",cartasUsuario)
print("Tu puntuacion es: ", puntuacion)
