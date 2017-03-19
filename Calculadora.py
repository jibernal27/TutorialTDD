# -*- coding: utf-8 -*-
_author_='Jairo'
class Calculadora:
    def sumar(self,cadena):
        if cadena=="":
            return 0
        elif "," in cadena:
            return int(cadena[0])+int(cadena[2])
        else:
            return int(cadena)