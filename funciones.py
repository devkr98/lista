from random import randint
from random import shuffle
import re



def barajar(baraja):
    #Esta funcion sirve para barajar un juego de cartas la funcion primero mezcla la baraja y despues me devuelve dos listas 1)con 
    mano = []
    shuffle(baraja)
    lenLista = len(baraja)
    mano.extend(baraja)
    return mano

def desglosaCarta(carta):
    cartaSelec = carta
    listaCad = list(cartaSelec)
    #aqui seleccionamos el tipo de palo.
    tipoPalo = listaCad[-1]
    #Aqui seleccionamos el numero del palo.
    tipoNumero = re.sub("\D", "", carta)
    tipoNumero = int(tipoNumero)

    return tipoPalo,tipoNumero

def reparteCartas(baraja):
    posicionAleatoria = 0
    cartasBarajadas = barajar(baraja)
    cartaAux = ""
    listaCartas = []

    for i in range(5):
        posicionAleatoria = randint(0,len(cartasBarajadas)-1)
        cartaAux = cartasBarajadas.pop(posicionAleatoria)
        listaCartas.append(cartaAux)
    return listaCartas

def puntosMazo(listaCartas):

    puntuacion = 0
    for carta in listaCartas:
        palo,numeroCarta = desglosaCarta(carta)
        if numeroCarta == 1:
            puntuacion += 11
        if numeroCarta == 3:
            puntuacion += 10
        if numeroCarta == 10:
            puntuacion += 2
        if numeroCarta == 11:
            puntuacion += 3
        if numeroCarta == 12:
            puntuacion += 4
        else:
            puntuacion += 0
    return puntuacion

def traduceBarajaEspañola(carta):

    tipoPalo,tipoNumero = desglosaCarta(carta)
    
    if tipoPalo == "B":
        if tipoNumero > 1 and tipoNumero<10:
            print(tipoNumero," de Bastos")
        if tipoNumero == 1:
            print("As de Bastos")
        if tipoNumero == 10:
            print("Sota de Bastos")
        if tipoNumero == 11:
            print("Caballo de Bastos")
        if tipoNumero == 12:
            print("Rey de Bastos")    
    if tipoPalo == "C":
        if tipoNumero > 1 and tipoNumero<10:
            print(tipoNumero," de Copas")
        if tipoNumero == 1:
            print("As de Copas")
        if tipoNumero == 10:
            print("Sota de Copas")
        if tipoNumero == 11:
            print("Caballo de Copas")
        if tipoNumero == 12:
            print("Rey de Copas")   
    if tipoPalo == "E":
        if tipoNumero > 1 and tipoNumero<10:
            print(tipoNumero," de Espadas")
        if tipoNumero == 1:
            print("As de Espadas")
        if tipoNumero == 10:
            print("Sota de Espadas")
        if tipoNumero == 11:
            print("Caballo de Espadas")
        if tipoNumero == 12:
            print("Rey de Espadas") 
    if tipoPalo == "O":
        if tipoNumero > 1 and tipoNumero<10:
            print(tipoNumero," de Oros")
        if tipoNumero == 1:
            print("As de Oros")
        if tipoNumero == 10:
            print("Sota de Oros")
        if tipoNumero == 11:
            print("Caballo de Oros")
        if tipoNumero == 12:
            print("Rey de Oros")

            
def traduceBarajaFrancesa(carta):

    tipoPalo,tipoNumero = desglosaCarta(carta)
    
    if tipoPalo == "D":
        if tipoNumero >= 2 and tipoNumero<=10:
            print(tipoNumero," de Diamantes")
        if tipoNumero == 11:
            print("(J) Jack de Diamantes")
        if tipoNumero == 12:
            print("(Q) Reina de Diamantes")
        if tipoNumero == 13:
            print("(K) Rey de Diamantes")
        if tipoNumero == 1:
            print("AS de Diamantes")
    if tipoPalo == "P":
        if tipoNumero >= 2 and tipoNumero<=10:
            print(tipoNumero," de Picas")
        if tipoNumero == 11:
            print("(J) Jack de Picas")
        if tipoNumero == 12:
            print("(Q) Reina de Picas")
        if tipoNumero == 13:
            print("(K) Rey de Picas")
        if tipoNumero == 1:
            print("AS de Picas")
    if tipoPalo == "T":
        if tipoNumero >= 2 and tipoNumero<=10:
            print(tipoNumero," de Treboles")
        if tipoNumero == 11:
            print("(J) Jack de Treboles")
        if tipoNumero == 12:
            print("(Q) Reina de Treboles")
        if tipoNumero == 13:
            print("(K) Rey de Treboles")
        if tipoNumero == 1:
            print("AS de Treboles")
    if tipoPalo == "C":
        if tipoNumero >= 2 and tipoNumero<=10:
            print(tipoNumero," de Corazones")
        if tipoNumero == 11:
            print("(J) Jack de Corazones")
        if tipoNumero == 12:
            print("(Q) Reina de Corazones")
        if tipoNumero == 13:
            print("(K) Rey de Corazones")
        if tipoNumero == 1:
            print("AS de Corazones")
