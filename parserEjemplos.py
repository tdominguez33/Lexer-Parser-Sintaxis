from lexer_TP1 import lexer
from parser_TP2 import traduccionParser, parser

cadenasEjemplo =[
    "mientras var esMenorQue 69 hacer op clp",
    "mostrar var",
    "si 2 entonces op clp sino op clp",
    "var1 eq var2",
    "mientras 69 esMenorQue(contador + 45)",
    "mientras x esMenorQue 4 hacer op aceptar var clp",
    "aceptar var",
    "x eq 69",
    "mostrar x * 9",
    "Si (num * id) * id + num entonces op aceptar var clp sino op mostrar var clp"
]
i = 1
for ejemplo in cadenasEjemplo:
    print("=============Cadena N°", i, "=============")
    parser(traduccionParser(lexer(ejemplo)))
    i += 1
