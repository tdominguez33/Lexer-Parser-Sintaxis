# Función que convierte la salida del lexer a una lista que el parser puede entender
def traduccionParser(salidaLexer):
    cadena = []
    # Ponemos cada primer elemento de cada tupla (token) en una lista
    for tupla in salidaLexer:
        cadena.append(tupla[0])
    cadena.append('#')
    return cadena

# Función que genera las derivaciones, recibe el elemento a derivar, en que cadena y por que se deriva
def generarDerivacion(topePila, produccionAnterior, derivacion):
    # Obtenemos en que posición se encuentra el elemento a derivar
    indice = produccionAnterior.index(topePila)
    # Eliminamos el elemento a derivar
    produccionAnterior.remove(topePila)
    # Damos vuelta la lista de 'derivacion' para que luego al insertarla quede en el orden original
    produccionReversed = []
    for i in derivacion:
        produccionReversed.insert(0, i)

    # Insertamos la lista dada vuelta en la cadena a derivar
    for i in produccionReversed:
        produccionAnterior.insert(indice, i)
    
    return produccionAnterior

# "Program -> Estructura Program" tiene como simbolos directrices a: mientras, si, mostrar, aceptar e id
# El EOF es el simbolo #

# tabla[Columna][Fila]
tabla = {
    'Program':{
        'mientras': ['Estructura', 'Program'], 
        'si':       ['Estructura', 'Program'], 
        'mostrar':  ['Estructura', 'Program'], 
        'aceptar':  ['Estructura', 'Program'], 
        'id':       ['Estructura', 'Program'], 
        'clp':      [], 
        '#':        []
    },
    'Estructura':{
        'mientras': ['mientras', 'id', 'esMenorQue', 'Valor', 'hacer', 'op', 'Program', 'clp'], 
        'si':       ['si', 'Expresion', 'entonces', 'op', 'Program', 'clp', 'sino', 'op', 'Program', 'clp'], 
        'mostrar':  ['mostrar', 'Expresion'], 
        'aceptar':  ['aceptar', 'id'], 
        'id':       ['id', 'eq', 'Expresion']
    },
    'Valor':{
        'id':       ['id'], 
        'num':      ['num']
    },
    'Expresion':{
        '(':        ['Termino', 'Expresion2'], 
        'id':       ['Termino', 'Expresion2'], 
        'num':      ['Termino', 'Expresion2']
    },
    'Expresion2':{
        '+':        ['+', 'Termino', "Expresion2"], 
        '#':        []
    },
    'Termino':{
        '(':        ['Factor', 'Termino2'], 
        'id':       ['Factor', 'Termino2'], 
        'num':      ['Factor', 'Termino2']
    },
    'Termino2':{
        '*':        ['*', 'Factor', 'Termino2'], 
        '#':        []
    },
    'Factor':{
        '(':        ['(', 'Expresion', ')'], 
        'id':       ['Valor'], 
        'num':      ['Valor']
    }
}

# Lista de terminales
VT = ['eq', 'id', 'num', '*', '+', 'op', 'clp', 'si', 'entonces', 'sino', 'mostrar', 'aceptar', 'mientras', 'esMenorQue', 'hacer', '(', ')']

# Función principal
def parser(cadena):
    # Iniciamos la pila con el simbolo EOF (#) y el simbolo distinguido
    pila = ['#', 'Program']
    simboloApuntado = 0
    # Lista donde se trabaja con las derivaciones en cada ciclo
    derivacion = ['Program']
    # Lista donde se guardan todas las derivaciones
    derivaciones = []

    # Flag para salir del ciclo principal
    continuar = True

    # Ciclo principal
    while continuar:
        # Actualizamos el valor del tope
        tope = pila[-1]

        # Condición de éxito
        if (tope == '#') and (cadena[simboloApuntado] == '#'):
            print("La cadena es aceptada por el lenguaje")
            print("Derivaciones:")
            for i in derivaciones:
                print(i)
            break
            
        if tope in VT:
            if tope == cadena[simboloApuntado]:
                # Consumimos el último elemento de la pila
                pila.pop()
                # Avanzamos el puntero en un elemento
                simboloApuntado += 1
            
            # Si no se cumple la condición salimos del ciclo
            else:
                continuar = False
                print("La cadena no pertenece al lenguaje")
        else:
            # Intentamos obtener el elemento de la tabla en la posición indicada
            try:
                produccionTabla = tabla[tope][cadena[simboloApuntado]]
                # Damos vuelta la producción
                produccionReversed = []
                for i in produccionTabla:
                    # Insertamos todos los elementos en la posición 0 de la nueva lista
                    produccionReversed.insert(0, i)
                # Consumimos el último elemento de la pila
                pila.pop()
                # Agregamos la producción dada vuelta a la pila
                pila.extend(produccionReversed)
                # Guardamos la derivación
                derivacion = generarDerivacion(tope, derivacion, produccionTabla)
                # El .copy() es necesario porque sino se copian las referencias y tendriamos una lista con 5 elementos iguales
                derivaciones.append(derivacion.copy())

            # Si hay error salimos del ciclo   
            except:
                continuar = False
                print("La cadena no pertenece al lenguaje")
