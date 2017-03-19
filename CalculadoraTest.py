# -*- coding: utf-8 -*-
from unittest import TestCase

from  Calculadora import Calculadora
class CalculadoraTest(TestCase):
    def test_sumar(self):
        self.assertEqual(Calculadora().sumar(""),0,"Cadena vacia")
    def test_sumar_unaCadena(self):
        self.assertEqual(Calculadora().sumar("1"),1,"Un número")
    def test_sumar_cadena_con_numero(self):
        self.assertEqual(Calculadora().sumar("1"),1,"Un número")
        self.assertEqual(Calculadora().sumar("2"),2,"Un número")
    def test_sumar_cadena_con_dos_numeros(self):
        self.assertEqual(Calculadora().sumar("1,3"),4,"Dos números")
    def test_sumar_cadenaConMultiplesNumeros(self):
        self.assertEqual(Calculadora().sumar("5,2,4,1"),12,"Multiples números")
