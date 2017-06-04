from funciones import barajar
from funciones import desglosaCarta
from funciones import traduceBarajaFrancesa
from funciones import puntosMazo
from funciones import reparteCartas
from resultados import res
from manos import poquer
from manos import Trio
from manos import Full
from manos import Pareja
from manos import Dobles
from manos import color
from manos import escalera
from manos import escaleraColor



from random import randint
from random import shuffle
import re


barajaFrancesa = ['2D','3D','4D','5D','6D','7D','8D','9D','10D','11D','12D','13D','1D','2T','3T','4T','5T','6T','7T','8T','9T','10T','11T','12T','13T','1T',
                  '2P','3P','4P','5P','6P','7P','8P','9P','10P','11P','12P','13P','1P','2C','3C','4C','5C','6C','7C','8C','9C','10C','11C','12C','13C','1C']

player1 = []
player2 = []



player1 = reparteCartas(barajaFrancesa)
player2 = reparteCartas(barajaFrancesa)

#Mostramos la baraja del primer Jugador (Player1)
print("====*Jugador 1 esta es tu baraja ===*")
for carta in player1:
    cartaAux = traduceBarajaFrancesa(carta)
print("************************************** \n" )  
#Mostramos la baraja del segundo Jugador (player2)
print("====*Jugador 2 esta es tu baraja ===*")
for carta in player2:
    cartaAux = traduceBarajaFrancesa(carta)
print("************************************** \n" )
    

resultado1,nombreMano1 = res(player1)
resultado2,nombreMano2 = res(player2)

print("Jugador 1 :",nombreMano1)
print("Jugador 2 :",nombreMano2)

cartas1 = []
cartas2 = []

for carta in player1:
    auxPalo,auxNum = desglosaCarta(carta)
    cartas1.append(auxNum)
for carta in player2:
    auxPalo,auxNum = desglosaCarta(carta)
    cartas2.append(auxNum)

player1max = max(cartas1)
player2max = max(cartas2)


    

    
if resultado1 > resultado2:
    jugador1()
if resultado2 > resultado1:
    print("\n WIN PLAYER 2")

if resultado1 == resultado2:
    print("TENEIS LA MISMA MANO ESTO SE RESUELVE A LA CARTA MAS ALTA")
    if player1max > player2max:
        print("Gana el jugados 1 con una carta mayor de: ",player1max)
    if player2max > player1max:
        print("Gana el jugados 2 con una carta mayor de: ",player2max)  
         

    

    



    






