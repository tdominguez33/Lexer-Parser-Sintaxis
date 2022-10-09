
derivaciones = []
lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]

#lista1.reverse()

derivaciones.append(lista1)
#derivaciones.append(lista2)

lista1.remove(1)
#print(lista1)

def generarDerivacion(tope, produccionAnterior, produccionSiguiente):
    if(produccionAnterior == []):
        return produccionSiguiente
    
    indice = produccionAnterior.index(tope)
    produccionAnterior.remove(tope)
    produccionSiguiente.reverse()
    for i in produccionSiguiente:
        produccionAnterior.insert(indice, i)
    
    return produccionAnterior

lista3 = ['Program', 'pene']

derivacion1 = generarDerivacion('Program', [], lista3)
print(derivacion1)

