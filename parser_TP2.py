# Convertimos la salida del lexer a una lista que el parser puede entender
from lexer_TP1 import lexer


def traduccionParser(salidaLexer):
    cadena = []
    for tupla in salidaLexer:
        cadena.append(tupla[0])
    cadena.append('#')
    return cadena

def generarDerivacion(topePila, produccionAnterior, produccionSiguiente):
    indice = produccionAnterior.index(topePila)
    produccionAnterior.remove(topePila)
    produccionReversed = []
    # Damos vuelta la lista de produccionSiguiente
    for i in produccionSiguiente:
        # Insertamos todos los elementos en la posición 0 de la nueva lista
        produccionReversed.insert(0, i)

    for i in produccionReversed:
        produccionAnterior.insert(indice, i)
    
    return produccionAnterior

# "Program -> Estructura Program" tiene como simbolos directrices a: mientras, si, mostrar, aceptar e id
# tabla[Columna][Fila]
# El EOF es el simbolo #
tabla = {
    'Program':{'mientras': ['Estructura', 'Program'], 'si': ['Estructura', 'Program'], 'mostrar': ['Estructura', 'Program'], 'aceptar': ['Estructura', 'Program'], 'id': ['Estructura', 'Program'], 'clp': [], '#': []},
    'Estructura':{'mientras': ['mientras', 'id', 'esMenorQue', 'Valor', 'hacer', 'op', 'Program', 'clp'], 'si': ['si', 'Expresion', 'entonces', 'op', 'Program', 'clp', 'sino', 'op', 'Program', 'clp'], 'mostrar': ['mostrar', 'Expresion'], 'aceptar': ['aceptar', 'id'], 'id': ['id', 'eq', 'Expresion']},
    'Valor':{'id': ['id'], 'num': ['num']},
    'Expresion':{'(': ['Termino', 'Expresion2'], 'id': ['Termino', 'Expresion2'], 'num': ['Termino', 'Expresion2']},
    'Expresion2':{'+': ['+', 'Termino', "Expresion2"], '#': []},
    'Termino':{'(': ['Factor', 'Termino2'], 'id': ['Factor', 'Termino2'], 'num': ['Factor', 'Termino2']},
    'Termino2':{'*': ['*', 'Factor', 'Termino2'], '#': []},
    'Factor':{'(': ['(', 'Expresion', ')'], 'id': ['Valor'], 'num': ['Valor']}
}

VT = ['eq', 'id', 'num', '*', '+', 'op', 'clp', 'si', 'entonces', 'sino', 'mostrar', 'aceptar', 'mientras', 'esMenorQue', 'hacer', '(', ')']


def parser(cadena):
    #Iniciamos la pila con el simbolo EOF y el simbolo distinguido
    pila = ['#', 'Program']
    simboloApuntado = 0

    derivacion = ['Program']
    derivaciones = []

    continuar = True
    error = False

    while continuar:
        tope = pila[-1]

        if (tope == '#') and (cadena[simboloApuntado] == '#'):
            print("La cadena es aceptada por el lenguaje")
            print("Derivaciones:")
            for i in derivaciones:
                print(i)
            break

        if tope in VT:
            if tope == cadena[simboloApuntado]:
                pila.pop()
                simboloApuntado += 1
            else:
                error = True
        else:
            try:
                produccionTabla = tabla[tope][cadena[simboloApuntado]]
                produccionReversed = []
                for i in produccionTabla:
                    # Insertamos todos los elementos en la posición 0 de la nueva lista
                    produccionReversed.insert(0, i)
                pila.pop()
                pila.extend(produccionReversed)
                derivacion = generarDerivacion(tope, derivacion, produccionTabla)
                # El .copy() es necesario porque sino se copian las referencias y tendriamos una lista con 5 elementos iguales
                derivaciones.append(derivacion.copy())
                
            except:
                error = True

        if (error):
            continuar = False
            print("La cadena no pertenece al lenguaje")
