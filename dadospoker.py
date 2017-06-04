from random import randint


def tiradaDados():
    valores = ["R","N","J","Q","K","A"]
    listaFinal = []
    lenLista = len(valores)
    
    for i in range(5):
        numeroAleatorio = aleatorio(lenLista)
        listaFinal.append(valores[numeroAleatorio])
    devuelveDistintos(listaFinal)

def devuelveDistintos(tirada):
    listAux = ""
    rep = 0
    auxPos = 0
    hayPareja = False
    auxEj = []
    auxEj.extend(tirada)
    auxNum = []
    for i in tirada:
        rep = tirada.count(i)
        if rep > 1 :
            listAux = tirada.pop(auxPos)
            hayPareja = pareja(rep)
        auxPos = auxPos + 1
    for i in auxEj:
        valor = valorDado(i)
        print (i,"->",valor)
        auxNum.append(valor)
                
    if hayPareja == True:
        print("Tienes una pareja en tu tirada !!")
        
    #Vamos a ordenar la lista de mayor a menor y enviar los numeros a una funcion
    #que determine cual es la mayor.

    auxNum = sorted(auxNum, reverse = True)

    d1 = auxNum.pop(0)
    d2 = auxNum.pop(0)
    
    comparaDados(d1,d1)
    
def comparaDados(d1,d2):
    if d1 > d2 :
        print(d1, "Es mayor")
    if d2 > d1 :
        print(d2, "Es mayor")
    if d1 == d2 :
        print("Ambos numeros mayores son iguales")
    
    
def pareja(rep):
    hayPareja = False
    if rep == 2:
        hayPareja = True
    return hayPareja 

        
def aleatorio(size):
    numero = randint(0,size-1)
    return numero
def valorDado(dado):
    valor = 0
    if dado == "N":
        valor = 1
        return valor
    if dado == "R":
        valor = 2
        return valor
    if dado == "J":
        valor = 3
        return valor
    if dado == "Q":
        valor = 4
        return valor
    if dado == "K":
        valor = 5
        return valor
    if dado == "A":
        valor = 6
        return valor
    

    
tiradaDados()    
