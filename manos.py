from funciones import desglosaCarta
'''
Code by: Kevin Rivera

'''



def poquer(cartas):
    numCartas = []
    auxNum = 0
    auxPalo = ""
    for carta in cartas:
        auxPalo,auxNum = desglosaCarta(carta)
        numCartas.append(auxNum)
    
        
    veces = 0
    hayPoker = False
    for carta in numCartas:
    
        veces = numCartas.count(carta)
        
        if veces >= 4:
            hayPoker = True
    return hayPoker
        

def Trio(cartas):
    numCartas = []
    auxNum = 0
    auxPalo = ""
    for carta in cartas:
        auxPalo,auxNum = desglosaCarta(carta)
        numCartas.append(auxNum)
    
        
    veces = 0
    hayTrio = False
    
    for carta in numCartas:
    
        veces = numCartas.count(carta)
        
        if veces >= 3:
            hayTrio = True
    return hayTrio


def Full(cartas):
    numCartas = []
    auxNum = 0
    auxPalo = ""
    dosnumeros = []
    for carta in cartas:
        auxPalo,auxNum = desglosaCarta(carta)
        numCartas.append(auxNum)
    
        
    veces = 0
    hayFull = False
    cartaRepetida = 0
    
    for carta in numCartas:
    
        veces = numCartas.count(carta)
        
        if veces >= 3:
            hayFull = True
            cartaRepetida = carta
    
    if hayFull == True:
        
        for carta in numCartas:
            if carta != cartaRepetida :
                dosnumeros.append(carta)
    
    for carta in dosnumeros:
        vecesdos = dosnumeros.count(carta)
        if vecesdos <= 1 :
            hayFull = False
        if vecesdos > 1 :
            hayFull = True
            
    return hayFull

def Pareja(cartas):
    numCartas = []
    auxNum = 0
    auxPalo = ""
    for carta in cartas:
        auxPalo,auxNum = desglosaCarta(carta)
        numCartas.append(auxNum)
    
        
    veces = 0
    hayPareja = False
    
    for carta in numCartas:
    
        veces = numCartas.count(carta)
        
        if veces == 2:
            hayPareja = True
    return hayPareja


def Dobles(cartas):
    numCartas = []
    auxNum = 0 
    auxPalo = ""
    auxlist = []
    veces = 0
    hayPareja = False
    hayDoblePareja = False
    auxnum = 0
    
    for carta in cartas:
        auxPalo,auxNum = desglosaCarta(carta)
        numCartas.append(auxNum)
    
    for carta in numCartas:
    
        veces = numCartas.count(carta)
        
        if veces == 2:
            auxnum = carta
            hayPareja = True
            
            break
    if hayPareja == True:
        for carta in numCartas:
            if carta != auxnum:
                auxlist.append(carta)
        for carta in auxlist:
            veces = auxlist.count(carta)
            if veces == 2:
                auxnum = carta
                hayDoblePareja = True
    return hayDoblePareja

def color(cartas):

    hayColor = False
    
    auxpalo = ""
    auxnum = 0
    palosNegros = []
    palosRojos = []
 
    for carta in cartas:
        auxpalo,auxnum = desglosaCarta(carta)
        if auxpalo == "D" or auxpalo == "C":
            palosRojos.append(auxpalo)
        if auxpalo == "P" or auxpalo == "T":
            palosNegros.append(auxpalo)
            
    listaNegra = len(palosNegros)
    listaRoja = len(palosRojos)
    

    if listaNegra == 5:
        hayColor = True
    if listaRoja == 5:
        hayColor = True
    
    return hayColor

def escalera(cartas):
    hayEscalera = False
    
    pv = True
    auxpalo = ""
    auxnum = 0
    auxCartas = []

    for carta in cartas:
        auxpalo,auxnum = desglosaCarta(carta)
        auxCartas.append(auxnum)
    sv = False
    auxCartas.sort()
    for carta in auxCartas:
        n = carta
        if sv == True:
            if nprev != carta - 1:
                hayEscalera = False
                break
            if nprev == carta -1:
                hayEscalera = True
        nprev = carta
        sv = True
    return hayEscalera
        
        
def escaleraColor(cartas):

    comprobadorColor = color(cartas)
    hayEscaleraColor = False

    
    if comprobadorColor == True:

        hayEscaleraColor = escalera(cartas)
        return hayEscaleraColor
        
        
    if comprobadorColor == False:
        hayEscaleraColor = False
        return hayEscaleraColor

    




    

    



























        
        
    
    
    
    
