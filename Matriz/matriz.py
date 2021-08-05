#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 10:19:38 2021

@author: jpg
"""

import numpy as np

''' Crear una matriz de 5x5 randomizada con números enteros, encontrar secuencia de 4 números consecutivos horizontal o vertical y si se encuentra mostrar la posición inicial y final '''

def busqueda_4_consecutivos(matriz, nRecorrido = 0):
    '''
    pre-condicion: dic debe ser una lista de diccionarios que contangan como claves las palabras 'id' y 'edad' y sus valores sean numeros enteros
    
    --- TEST **hacerlo mejor requeriria mayor tiempo para realizar varios try-except** ---
    >>> busqueda_4_consecutivos([[1,2,3,4,5],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]])
    {'busqueda': 'horizontal', 'posicion_inicial': (0, 0), 'posicion_final': (0, 3)}
    
    >>> busqueda_4_consecutivos([[1,1,1,1,1],[2,1,1,1,1],[3,1,1,1,1],[4,1,1,1,1],[5,1,1,1,1]])
    {'busqueda': 'vertical', 'posicion_inicial': (0, 0), 'posicion_final': (3, 0)}
    
    >>> busqueda_4_consecutivos([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]])
    False
    
    Parameters
    ----------
    matriz : numpy.ndarray | list
        Debe ser una matriz cuadrada.
    nRecorrido : int, optional
        Es un control interno para realizar la busqueda tanto horizontal como verticalmente. Puede indicarse el valor 1 para realizar la busqueda solo horizonalmente. The default is 0.

    Returns
    -------
    dict | bool
        En caso de encontrar 4 numeros consecutivos, devuelve un diccionario con la direccion en la que se encontro y la posicion inicial y final de los elementos. Caso contrario devuelve el booleano False

    '''
    for x in range(len(matriz)):
        nConsecutivos = 1
        
        for y in range(len(matriz) - 1):
            if matriz[x][y]+1 == matriz[x][y+1]:
                nConsecutivos += 1
                
            else:
                nConsecutivos = 1
                
            if nConsecutivos == 4:
                if nRecorrido == 0:
                    return {'busqueda': 'horizontal', 'posicion_inicial': (x, y-2), 'posicion_final':(x, y+1)}
                
                return {'busqueda': 'vertical', 'posicion_inicial': (y-2, x), 'posicion_final':(y+1, x)}
    
    if nRecorrido == 0:
        return busqueda_4_consecutivos(np.transpose(matriz), 1)

    return False
    
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    matriz = np.random.randint(4, size=(5, 5))
    resultado = busqueda_4_consecutivos(matriz)
    if(resultado):
        print (f"Se encontraron 4 numeros consecutivos en forma {resultado['busqueda']} desde la posicion {resultado['posicion_inicial']} hasta la posicion {resultado['posicion_final']}")
    else:
        print('no existe 4 numeros consecutivos en ninguna direccion')

