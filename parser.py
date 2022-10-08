# Comunicación entre el lexer y el parser
from lexer import lexer

cadena = []

resultadoLexer = lexer("mientras 69 esMenorQue 70 hacer op clp")

for tup in resultadoLexer:
    cadena.append(tup[0])

cadena.append('#')

print(cadena)

#"Program -> Estructura Program" me puede generar: mientras, si, mostrar, aceptar e id
# tabla[Columna][Fila]
# El EOF es el simbolo #
tabla = {
    'Program':{'mientras': ['Estructura', 'Program'], 'si': ['Estructura', 'Program'], 'mostrar': ['Estructura', 'Program'], 'aceptar': ['Estructura', 'Program'], 'id': ['Estructura', 'Program'], 'EOF': []},
    'Estructura':{'mientras': ['mientras', 'id', 'esMenorQue', 'Valor', 'hacer', 'op', 'Program', 'clp'], 'si': ['si', 'Expresion', 'entonces', 'op', 'Program', 'clp', 'sino', 'op', 'Program', 'clp'], 'mostrar': ['mostrar', 'Expresion'], 'aceptar': ['aceptar', 'id'], 'id': ['id', 'eq', 'Expresion']},
    'Valor':{'id': ['id'], 'num': ['num']},
    'Expresion':{'(': ['Termino', 'Expresion2']},
    'Expresion2':{'+': ['+', 'Termino', "Expresion2"], 'EOF': []},
    'Termino':{'(': ['Factor', 'Termino2']},
    'Termino2':{'*': ['*', 'Factor', 'Termino2'], 'EOF': []},
    'Factor':{'(': ['(', 'Expresion', ')'], 'id': ['Valor'], 'num': ['Valor']}
}

VT = ['eq', 'id', 'num', '*', '+', 'op', 'clp', 'si', 'entonces', 'sino', 'mostrar', 'aceptar', 'mientras', 'esMenorQue', 'hacer', '(', ')']

#Iniciamos la pila con el simbolo EOF y el simbolo distinguido
pila = ['#', 'Program']

puntero = 0

derivaciones = []

continuar = True
error = False
while (continuar):
    tope = pila[-1]

    if tope in VT:
        if tope == cadena[puntero]:
            pila.pop()
            puntero += 1
        else:
            error = True
    else:
        try:
            produccionTabla = tabla[tope][cadena[puntero]]
            derivaciones.append(produccionTabla)
            produccionTabla.reverse()
            pila.pop()
            pila.extend(produccionTabla)
            
        except:
            error = True

    if (tope == '#') and (cadena[puntero] == '#'):
        continuar = False
    
    if (error):
        continuar = False
        print("Error")
