#Examen ProgramacionI - Ej4

def main():
    programa_terminado = False
    while programa_terminado == False:
        lista_numeros = []
        lista_pares_impares = []
        cantidad_numeros = int(input('Inserte la cantidad de numeros que desea mandarle al programa: '))
    
        for x in range(cantidad_numeros):
            numero = int(input('Inserte un numero: '))
            lista_numeros.append(numero)
    
        lista_numeros.sort(reverse = False)
    
        for y in range(len(lista_numeros)):
            for z in range(len(lista_numeros)):
                if lista_numeros[y]==lista_numeros[z] and (y != z) and (lista_numeros[y] and lista_numeros[z] not in lista_pares_impares): #Si esta repetido y no esta en lista pares impares
                    if lista_numeros[z] % 2 == 0: #Si es par
                        lista_pares_impares.append(lista_numeros[z])
                    elif lista_numeros[z] % 2: #Si es impar
                        lista_pares_impares.append(lista_numeros[y]-1)
                    else:
                    	lista_numeros = lista_numeros
                else:
                    lista_numeros = lista_numeros

        for a in range(len(lista_pares_impares)):
        	lista_numeros.append(lista_pares_impares[a])

        print(lista_numeros)

        eleccion = int(input('Inserte el numero 0 si desea terminar el programa.'))
        if eleccion != 0:
            programa_terminado = False
        else:
            programa_terminado = True

main()