# El Lexer le envia los tokens al Parser, solo se preocupa de que los tokens esten bien formados.
# Cada token representa un grupo de terminales de la gramática
# Lexema: Valor que toma el token en esa posición
# Los números son solo enteros
import automatas
from automatas import FINAL
from automatas import NOFINAL

# Lista de posibles tokens en orden de jerarquia
TOKENS_POSIBLES = [("eq", automatas.afd_eq), ("num", automatas.afd_num), ("+", automatas.afd_suma) , ("*", automatas.afd_multiplicacion), ("op", automatas.afd_abrirParentesis), ("clp", automatas.afd_cerrarParentesis), ("si", automatas.afd_si), ("entonces", automatas.afd_entonces), ("sino", automatas.afd_sino), ("mostrar", automatas.afd_mostrar), ("aceptar", automatas.afd_aceptar), ("mientras", automatas.afd_mientras), ("esMenorQue", automatas.afd_esMenorQue), ("hacer", automatas.afd_hacer), ("id", automatas.afd_id)]

#print(TOKENS_POSIBLES[0][1]("si"))

tokens = []

# Devuelve si cierta cadena genera que todos los automatas queden en un estado trampa
def generaEstadosTrampa(cadena):
    todosEstadosTrampa = True

    # Corremos la cadena en todos los automatas
    for (tipoToken, afd) in TOKENS_POSIBLES:
        resultado = afd(cadena)
        # Si aunque sea un autómata queda en estado final o no final podemos salir
        if resultado == (FINAL or NOFINAL):
            todosEstadosTrampa = False
            break
    
    return todosEstadosTrampa

# Guardar el token de la cadena en la variable 'tokens'
def guardarToken(cadena):
    global tokens

    # Corremos la cadena en todos los automatas
    for (tipoToken, afd) in TOKENS_POSIBLES:
        resultado = afd(cadena)

        # Guardamos solo el primero que aparezca
        if resultado == (FINAL):
            tokens.append((tipoToken, cadena))
            break

def lexer(codigoFuente):
    # Agregamos un espacio para que pueda detectar correctamente el final de linea
    codigoFuente += ' '
    global tokens
    tokens = []
    tokensDesconocidos = []
    inicio = 0
    final = 1
    while final <= len(codigoFuente):
        lexema = codigoFuente[inicio : final]
        
        # Mientras no se generen estados trampa en todos los automatas seguimos añadiendo caracteres al lexema hasta que nos pasemos
        while not generaEstadosTrampa(lexema):
            final += 1
            lexema = codigoFuente[inicio : final]
        
        # Como nos pasamos volvemos al estado anterior y guardamos el token que le corresponde
        final -= 1
        guardarToken(codigoFuente[inicio : final])
        
        # Se usa para evitar un ciclo infinito en los tokens desconocidos
        if inicio == final:
            tokensDesconocidos.append(codigoFuente[inicio : final + 1])
            inicio += 1
            final += 2
        else:
            inicio = final
            final = inicio + 1

        # Si no quedan mas caracteres en el código fuente salimos del while, pero antes chequeamos que no nos haya quedado nada

        if final == len(codigoFuente):
            break
        
    print("Token/s desconocidos: " + str(tokensDesconocidos))
    return tokens

print(lexer("mientras 92 esMenorQue 45"))
