# -*- coding: utf-8 -*-
_author_='Jairo'
class Calculadora:
    def sumar(self,cadena):
        if cadena=="":
            return 0
        elif "," in cadena:
            suma=0
            numeros=cadena.split(",")
            for num in numeros:
                suma+=int(num)
            return suma
        else:
            return int(cadena)