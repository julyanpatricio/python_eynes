#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 11:20:07 2021

@author: jpg
"""

''' Escribir una clase en python llamada círculo que contenga un radio, con un método que
devuelva el área y otro que devuelva el perímetro del círculo.
Si se instancia la clase con radio <= 0 mostrar una excepción indicando un error amigable al usuario e impidiendo la instanciación.
Si printeamos el objeto creado debe mostrarse una representación amigable.
El objeto debe tener su atributo radio modificable, si se le intenta setear un valor <= 0
mostrar un error y no permitir modificación.
Permitir la multiplicación del circulo: Circulo * n debe devolver un nuevo objeto con el radio multiplicado por n. No permitir la multiplicación por números <= 0 '''
import math

class Circulo:
    def __init__(self, valor):
        if valor <= 0:
            raise ValueError(f'El radio debe ser mayor a cero')
        self._radio = valor
        

    def __str__(self): #legible
        return f'Circulo de radio {self.radio}, con area de {self.area():.2f} y perimetro de {self.perimetro():.2f}'
    
    def __repr__(self): #representativo
        return '{self.__class__.__name__}({self.radio})'.format(self=self)
    
    @property
    def radio(self):
        return self._radio
    
    @radio.setter
    def radio(self, valor):
        if valor <= 0:
            raise ValueError(f'El radio debe ser mayor a cero')
        self._radio = valor
    
    def area(self):
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.radio
    
    def __mul__(self, n):
        if n <= 0:
            raise ValueError(f'El radio debe ser mayor a cero')
        return Circulo(self.radio * n)
