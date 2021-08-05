import random 



''' Hacer una función que genere una lista de diccionarios que contengan id y edad, donde
edad sea un número aleatorio entre 1 y 100 y la longitud de la lista sea de 10
elementos. retornar la lista. '''
def lista_diccionarios():
    return [{'id':i+1, 'edad':random.randint(1,100)} for i in range(100)]


''' Hacer otra función que reciba lo generado en la primer función y ordenarlo de mayor amenor. Printear el id de la persona más joven y más vieja. Devolver la lista ordenada. ''' 
def ord_div(lista):
    ''' divide los elementos de la lista recursivamente'''
    if len(lista) <     2:
        return lista
    medio = len(lista) // 2
    izq = ord_div(lista[:medio])
    der = ord_div(lista[medio:])
    return unir_en_orden(izq, der)
    

def unir_en_orden(lista1, lista2):
    '''#Intercala los elementos de lista1 y lista2 de forma ordenada.'''
    i, j = 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i]['edad'] > lista2[j]['edad']):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado


def busqueda_diccionario(dic):
    '''
    pre-condicion: dic debe ser una lista de diccionarios que contangan como claves las palabras 'id' y 'edad' y sus valores sean numeros enteros
    
    --- TEST **hacerlo mejor requeriria mayor tiempo para realizar varios try-except** ---
    >>> busqueda_diccionario([{'id':1, 'edad':25},{'id':2, 'edad':100},{'id':3, 'edad':9},{'id':4, 'edad':1}])
    {'id_persona_joven': 4, 'id_persona_vieja': 2}
    '''
    
    lista_ordenada = ord_div(dic)
    return {'id_persona_joven':lista_ordenada[-1]['id'], 'id_persona_vieja':lista_ordenada[0]['id']}



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    dic= lista_diccionarios()
resultado = busqueda_diccionario(dic)
print(f"El id de la persona mas joven y de la mas vieja es {resultado['id_persona_joven']} y {resultado['id_persona_vieja']} respectivamente")