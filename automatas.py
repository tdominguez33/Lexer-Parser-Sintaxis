LETRAS_MINUSCULAS   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
LETRAS_MAYUSCULAS   = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
NUMEROS             = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

FINAL = "Autómata en estado FINAL"
NOFINAL = "Autómata en estado NO FINAL"
TRAMPA = "Autómata en estado TRAMPA"

# eq -> Signo =
def afd_eq(cadena):
    estadoActual = 0
    estadosFinales = [1]
    
    for caracter in cadena:
        if estadoActual == 0 and caracter == '=':
            estadoActual = 1
        else:
            estadoActual = -1
            return TRAMPA
    
    if estadoActual in estadosFinales:
        return FINAL
    else:
        return NOFINAL

# Los id's tienen que comenzar una letra y luego puede tener combinación de letras y números
def afd_id(cadena):
    estadoActual = 0
    estadosFinales = [1]
    
    for caracter in cadena:
        if estadoActual == 0 and ((caracter in LETRAS_MINUSCULAS) or (caracter in LETRAS_MAYUSCULAS)):
            estadoActual = 1
        elif estadoActual == 1 and ((caracter in LETRAS_MINUSCULAS) or (caracter in LETRAS_MAYUSCULAS) or (caracter in NUMEROS)):
            estadoActual = 1
        else:
            estadoActual = -1
            return TRAMPA
    
    if estadoActual in estadosFinales:
        return FINAL
    else:
        return NOFINAL

# num -> Cualquier Número
def afd_num(cadena):
    estadoActual = 0
    estadosFinales = [1]
    
    for caracter in cadena:
        if estadoActual == 0 and (caracter in NUMEROS):
            estadoActual = 1
        elif estadoActual == 1 and caracter in NUMEROS:
            estadoActual = 1
        else:
            estadoActual = -1
            return TRAMPA
    
    if estadoActual in estadosFinales:
        return FINAL
    else:
        return NOFINAL

# multiplicacion -> signo *
def afd_multiplicacion(cadena):
    estadoActual = 0
    estadosFinales = [1]
    
    for caracter in cadena:
        if estadoActual == 0 and caracter == "*":
            estadoActual = 1
        else:
            estadoActual = -1
            return TRAMPA
    
    if estadoActual in estadosFinales:
        return FINAL
    else:
        return NOFINAL

def afd_abrirParentesis(cadena):
    estadoActual = 0
    estadosFinales = [1]
    
    for caracter in cadena:
        if estadoActual == 0 and caracter == "(":
            estadoActual = 1
        else:
            estadoActual = -1
            return TRAMPA
    
    if estadoActual in estadosFinales:
        return FINAL
    else:
        return NOFINAL

def afd_cerrarParentesis(cadena):
    estadoActual = 0
    estadosFinales = [1]
    
    for caracter in cadena:
        if estadoActual == 0 and caracter == ")":
            estadoActual = 1
        else:
            estadoActual = -1
            return TRAMPA
    
    if estadoActual in estadosFinales:
        return FINAL
    else:
        return NOFINAL

# suma -> signo +
def afd_suma(cadena):
    estadoActual = 0
    estadosFinales = [1]
    
    for caracter in cadena:
        if estadoActual == 0 and caracter == "+":
            estadoActual = 1
        else:
            estadoActual = -1
            return TRAMPA
    
    if estadoActual in estadosFinales:
        return FINAL
    else:
        return NOFINAL

def afd_si(cadena):
    estadoActual = 0
    estadosFinales = [2]
    
    for caracter in cadena:
        if estadoActual == 0 and caracter == 's':
            estadoActual = 1
        elif estadoActual == 1 and caracter == 'i':
            estadoActual = 2
        else:
            estadoActual = -1
            return TRAMPA
    
    if estadoActual in estadosFinales:
        return FINAL
    else:
        return NOFINAL

def afd_entonces(cadena):
    estadoActual = 0
    estadosFinales = [8]
    
    for caracter in cadena:
        if estadoActual == 0 and caracter == 'e':
            estadoActual = 1
        elif estadoActual == 1 and caracter == 'n':
            estadoActual = 2
        elif estadoActual == 2 and caracter == 't':
            estadoActual = 3
        elif estadoActual == 3 and caracter == 'o':
            estadoActual = 4
        elif estadoActual == 4 and caracter == 'n':
            estadoActual = 5
        elif estadoActual == 5 and caracter == 'c':
            estadoActual = 6
        elif estadoActual == 6 and caracter == 'e':
            estadoActual = 7
        elif estadoActual == 7 and caracter == 's':
            estadoActual = 8
        else:
            estadoActual = -1
            return TRAMPA
    
    if estadoActual in estadosFinales:
        return FINAL
    else:
        return NOFINAL

def afd_sino(cadena):
    estadoActual = 0
    estadosFinales = [4]
    
    for caracter in cadena:
        if estadoActual == 0 and caracter == 's':
            estadoActual = 1
        elif estadoActual == 1 and caracter == 'i':
            estadoActual = 2
        elif estadoActual == 2 and caracter == 'n':
            estadoActual = 3
        elif estadoActual == 3 and caracter == 'o':
            estadoActual = 4
        else:
            estadoActual = -1
            return TRAMPA
    
    if estadoActual in estadosFinales:
        return FINAL
    else:
        return NOFINAL

def afd_mostrar(cadena):
    estadoActual = 0
    estadosFinales = [7]
    
    for caracter in cadena:
        if estadoActual == 0 and caracter == 'm':
            estadoActual = 1
        elif estadoActual == 1 and caracter == 'o':
            estadoActual = 2
        elif estadoActual == 2 and caracter == 's':
            estadoActual = 3
        elif estadoActual == 3 and caracter == 't':
            estadoActual = 4
        elif estadoActual == 4 and caracter == 'r':
            estadoActual = 5
        elif estadoActual == 5 and caracter == 'a':
            estadoActual = 6
        elif estadoActual == 6 and caracter == 'r':
            estadoActual = 7
        else:
            estadoActual = -1
            return TRAMPA
    
    if estadoActual in estadosFinales:
        return FINAL
    else:
        return NOFINAL

def afd_aceptar(cadena):
    estadoActual = 0
    estadosFinales = [7]
    
    for caracter in cadena:
        if estadoActual == 0 and caracter == 'a':
            estadoActual = 1
        elif estadoActual == 1 and caracter == 'c':
            estadoActual = 2
        elif estadoActual == 2 and caracter == 'e':
            estadoActual = 3
        elif estadoActual == 3 and caracter == 'p':
            estadoActual = 4
        elif estadoActual == 4 and caracter == 't':
            estadoActual = 5
        elif estadoActual == 5 and caracter == 'a':
            estadoActual = 6
        elif estadoActual == 6 and caracter == 'r':
            estadoActual = 7
        else:
            estadoActual = -1
            return TRAMPA
    
    if estadoActual in estadosFinales:
        return FINAL
    else:
        return NOFINAL

def afd_mientras(cadena):
    estadoActual = 0
    estadosFinales = [8]
    
    for caracter in cadena:
        if estadoActual == 0 and caracter == 'm':
            estadoActual = 1
        elif estadoActual == 1 and caracter == 'i':
            estadoActual = 2
        elif estadoActual == 2 and caracter == 'e':
            estadoActual = 3
        elif estadoActual == 3 and caracter == 'n':
            estadoActual = 4
        elif estadoActual == 4 and caracter == 't':
            estadoActual = 5
        elif estadoActual == 5 and caracter == 'r':
            estadoActual = 6
        elif estadoActual == 6 and caracter == 'a':
            estadoActual = 7
        elif estadoActual == 7 and caracter == 's':
            estadoActual = 8
        else:
            estadoActual = -1
            return TRAMPA
    
    if estadoActual in estadosFinales:
        return FINAL
    else:
        return NOFINAL

def afd_esMenorQue(cadena):
    estadoActual = 0
    estadosFinales = [10]
    
    for caracter in cadena:
        if estadoActual == 0 and caracter == 'e':
            estadoActual = 1
        elif estadoActual == 1 and caracter == 's':
            estadoActual = 2
        elif estadoActual == 2 and caracter == 'M':
            estadoActual = 3
        elif estadoActual == 3 and caracter == 'e':
            estadoActual = 4
        elif estadoActual == 4 and caracter == 'n':
            estadoActual = 5
        elif estadoActual == 5 and caracter == 'o':
            estadoActual = 6
        elif estadoActual == 6 and caracter == 'r':
            estadoActual = 7
        elif estadoActual == 7 and caracter == 'Q':
            estadoActual = 8
        elif estadoActual == 8 and caracter == 'u':
            estadoActual = 9
        elif estadoActual == 9 and caracter == 'e':
            estadoActual = 10
        else:
            estadoActual = -1
            return TRAMPA
    
    if estadoActual in estadosFinales:
        return FINAL
    else:
        return NOFINAL

def afd_hacer(cadena):
    estadoActual = 0
    estadosFinales = [5]
    
    for caracter in cadena:
        if estadoActual == 0 and caracter == 'h':
            estadoActual = 1
        elif estadoActual == 1 and caracter == 'a':
            estadoActual = 2
        elif estadoActual == 2 and caracter == 'c':
            estadoActual = 3
        elif estadoActual == 3 and caracter == 'e':
            estadoActual = 4
        elif estadoActual == 4 and caracter == 'r':
            estadoActual = 5
        else:
            estadoActual = -1
            return TRAMPA
    
    if estadoActual in estadosFinales:
        return FINAL
    else:
        return NOFINAL

# No estoy seguro
def afd_tupla(cadena):
    estadoActual = 0
    estadosFinales = [4]
    
    for caracter in cadena:
        if estadoActual == 0 and caracter == '(':
            estadoActual = 1
        elif estadoActual == 1 and caracter == ',':
            estadoActual = 2
        elif estadoActual == 2 and caracter == ' ':
            estadoActual = 3
        elif estadoActual == 3 and caracter == ')':
            estadoActual = 4
        else:
            estadoActual = -1
            return TRAMPA
    
    if estadoActual in estadosFinales:
        return FINAL
    else:
        return NOFINAL
