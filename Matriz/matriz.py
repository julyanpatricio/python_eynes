#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 10:19:38 2021

@author: jpg
"""

import numpy as np

''' Crear una matriz de 5x5 randomizada con números enteros, encontrar secuencia de 4 números consecutivos horizontal o vertical y si se encuentra mostrar la posición inicial y final '''

def busqueda_4_consecutivos(matriz, nRecorrido = 0):
    for x in range(matriz.shape[0]):
        nConsecutivos = 1
        
        for y in range(matriz.shape[1] - 1):
            if matriz[x][y]+1 == matriz[x][y+1]:
                nConsecutivos += 1
                
            else:
                nConsecutivos = 1
                
            if nConsecutivos == 4:
                if nRecorrido == 0:
                    return f"La posicion inicial es ({x},{y-2}) y la final ({x},{y+1})"
                
                return f" en traspose La posicion inicial es ({y-2},{x}) y la final ({y+1},{x})"
    
    if nRecorrido == 0:
        
        return busqueda_4_consecutivos(np.transpose(matriz), 1)

    return 'no existe 4 numeros consecutivos en ninguna direccion'
    
        

matriz = np.random.randint(4, size=(5, 5))
print(busqueda_4_consecutivos(matriz))

matriz2 = np.transpose(np.array([
    [1,2,3,4,5],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1]]))
print(busqueda_4_consecutivos(matriz2))