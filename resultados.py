from manos import poquer
from manos import Trio
from manos import Full
from manos import Pareja
from manos import Dobles
from manos import color
from manos import escalera
from manos import escaleraColor



def res(barajaazar):

    #Orden de prioridad de manos.
    puntuacionescaleracolor = 1
    puntuacionpoqer = 2
    puntuacionfull = 3
    puntuacioncolor = 4
    puntuacionescalera = 5
    puntuaciontrio = 6
    puntuaciondoble = 7
    puntuacionpareja = 8
    puntuacioncartaalta = 0

    textoescaleracolor = "Su mayor mano es: Escalera de Color "
    textopoqer = "Su mayor mano es: Un Poker "
    textofull = "Su mayor mano es: Un Full "
    textocolor = "Su mayor mano es: Mano de color "
    textoescalera = "Su mayor mano es: Una Escalera "
    textotrio = "Su mayor mano es: Un trio "
    textodoble = "Su mayor mano es: Dobles cartas "
    textopareja = "Su mayor mano es: Una pareja "
    textocartaalta = "Lo siento no tiene ninguna mano "
    for i in range(1):
        
        #Vamos a comprobar si hay escalera de color
        
        hayEscaleraColor = escaleraColor(barajaazar)
        if hayEscaleraColor == True:
            
            return puntuacionescaleracolor,textoescaleracolor
            break
        

        #Vamos a comprobar si hay poquer
        
        hayPoker = poquer(barajaazar)
        if hayPoker == True:
            
            return puntuacionpoqer,textopoqer
            break
        

        #Vamos a comprobar sin el mano existe un full
        
        hayFull = Full(barajaazar)
        if hayFull == True:
            
            return puntuacionfull,textofull
            break
     

        #Vamos a comprobar si en la mano existe una mano de color
        
        hayColor = color(barajaazar)
        if hayColor == True:
            
            return puntuacioncolor,textocolor
            break
        

        #Vamos a comprobar si hay escalera
        
        hayEscalera = escalera(barajaazar)
        if hayEscalera == True:
            
            return puntuacionescalera,textoescalera
            break
        

        #Vamos a comprobar si en la mano existe una mano de Trio
           
        hayTrio = Trio(barajaazar)
        if hayTrio == True:
            
            return puntuaciontrio,textotrio
            break
        

        #Vamos a comprobar si en la mano existen dobles
          
        hayDoble = Dobles(barajaazar)
        if hayDoble == True:
            
            return puntuaciondoble,textodoble
            break
        
            
        #Vamos a comprobar si en la mano existe una pareja
        
        hayPareja = Pareja(barajaazar)
        if hayPareja == True:
            
            return puntuacionpareja,textopareja
            break
        if hayPareja == False:

            return puntuacioncartaalta,textocartaalta
            break
        
        
