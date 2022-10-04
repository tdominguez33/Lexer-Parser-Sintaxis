#"Program -> Estructura Program" me puede generar: mientras, si, mostrar, aceptar e id
# tabla[Columna][Fila]
# El EOF es el simbolo #
tabla = {
    'Program':{'mientras': ['Estructura', 'Program'], 'si': ['Estructura', 'Program'], 'mostrar': ['Estructura', 'Program'], 'aceptar': ['Estructura', 'Program'], 'id': ['Estructura', 'Program']},
    'Estructura':{'mientras': ['mientras', 'id', 'esMenorQue', 'Valor', 'hacer', 'op', 'Program', 'clp'], 'si': ['si', 'Expresion', 'entonces', 'op', 'Program', 'clp', 'sino', 'op', 'Program', 'clp'], 'mostrar': ['mostrar', 'Expresion'], 'aceptar': ['aceptar', 'id'], 'id': ['id', 'eq', 'Expresion']},
    'Valor':{'id': ['id'], 'num': ['num']},
    'Expresion':{'(': ['Termino', 'Expresion2']},
    'Expresion2':{'+': ['+', 'Termino', "Expresion2"], '#': []},
    'Termino':{'(': ['Factor', 'Termino2']},
    'Termino2':{'*': ['*', 'Factor', 'Termino2'], '#': []},
    'Factor':{'(': ['(', 'Expresion', ')'], 'id': ['Valor'], 'num': ['Valor']}
}

#Iniciamos la pila con el simbolo EOF y el simbolo distinguido
pila = ['#', 'S']

puntero = 0

derivaciones = []