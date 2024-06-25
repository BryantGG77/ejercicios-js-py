
# Ejercicio 3 - Es un palindromo?, en este ejercicio tienes que introducir una frase y te devolvera si es palindromo o no. basicamente lo que hace es invertir la frase y compararla con la original, ya que sera un palindromo si la frase es igual a la invertida.

def es_palindromo(frase):

    fraseLower = frase.lower().replace(" ", "")
    fraseInverted = fraseLower[::-1]
    
    resultado = True if fraseInverted == fraseLower else False
    return resultado
    