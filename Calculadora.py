# -*- coding: utf-8 -*-
_author_='Jairo'
class Calculadora:
    def sumar(self,cadena):
        if cadena=="":
            return 0
        elif "," or ":" or "&"in cadena:
            suma=0
            cadena=cadena.replace(":",",")
            cadena = cadena.replace("&", ",")
            numeros=cadena.split(",")
            for num in numeros:
                suma+=int(num)
            return suma
        else:
            return int(cadena)