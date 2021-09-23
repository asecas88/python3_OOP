#Escribir una clase en python que convierta un número entero a número romano    


class Conversor(object):

    def __init__(self):

        self.dict_unidad = {1 : 'I', 2 : 'II', 3 : 'III', 4 : 'IV', 5 :'V', 6 : 'VI', 7 : 'VII', 8 : 'VIII', 9 : 'IX', 0 : ''} 

        self.dict_decena = {1 : 'X', 2 : 'XX', 3 : 'XXX', 4 : 'XL', 5 : 'L', 6 : 'LX', 7 : 'LXX', 8 : 'LXXX', 9 : 'XC', 0 : ''}

        self.dict_centena = {1 : 'C', 2 : 'CC', 3 : 'CCC', 4 : 'CD', 5 : 'D', 6 : 'DC', 7 : 'DCC', 8 : 'DCCC', 9 : 'CM', 0 : ''}

        self.dict_milesima = {1 : 'M', 2 : 'MM', 3 : 'MMM', 0 : ''}   

    def milesima(self, pos):

        aux = int(entero[pos])

        return self.dict_milesima[aux]

    def centena(self, pos):

        aux = int(entero[pos])

        return self.dict_centena[aux]

    def decena(self, pos):

        aux = int(entero[pos])

        return self.dict_decena[aux]

    def unidad(self, pos):

        aux = int(entero[pos])

        return self.dict_unidad[aux]

# -----------------------------------------------------------

conv = Conversor()

print("Conversor arabigo-romano (0-3999)")

ingreso = input("Ingrese nro entero: ")          # '123' 

entero = list(ingreso)                           # ['1', '2', '3']

if len(entero) == 4:

    print('\n' + ingreso + '  >  ' + conv.milesima(0) + conv.centena(1) + conv.decena(2) + conv.unidad(3))

elif len(entero) == 3:
      
    print('\n' + ingreso + '  >  ' + conv.centena(0) + conv.decena(1) + conv.unidad(2))

elif len(entero) == 2:

    print('\n' + ingreso + '  >  ' + conv.decena(0) + conv.unidad(1))

else:

    print('\n' + ingreso + '  >  ' + conv.unidad(0))



                
