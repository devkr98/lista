from funciones import barajar
from funciones import desglosaCarta
from funciones import traduceCarta
from funciones import puntosMazo
from funciones import reparteCartas
from random import randint
from random import shuffle
import re

barajaEspañola = ['1B','2B','3B','4B','5B','6B','7B','8B','9B','10B','11B','12B','1C','2C','3C','4C','5C','6C','7C','8C','9C','10C','11C','12C',
          '1E','2E','3E','4E','5E','6E','7E','8E','9E','10E','11E','12E','10','2O','3O','4O','5O','6O','7O','8O','9O','10O','11O','12O']
barajaFrancesa = ['2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD','AD','2T','3T','4T','5T','6T','7T','8T','9T','10T','JT','QT','KT','AT',
                  '2P','3P','4P','5P','6P','7P','8P','9P','10P','JP','QP','KP','AP','2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC','AC']


barajaFrancesa = barajar(barajaFrancesa)

#Mezclar Baraja

print(barajaFrancesa)

    
