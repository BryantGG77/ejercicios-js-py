#En este ejercicio tienes una variable "lista" la cual contiene una lista de numeros aleatorios y el programa debes devolver una nueva lista con solo los números primos de la lista original.


def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def numeros_primos(lista):
    primos = []
    for numero in lista:
        if es_primo(numero):
            primos.append(numero)
    return primos