#En este ejercicio tienes que crear una función que te devolvera el factorial de un numero. (recuerda que el factorial es la multiplicación de todos los enteros positivos menores o iguales que el mismo)

def factorial(num):
    try:
        num_factorial = 1
        assert int(num) > 0
        for i in range(1, num+1):
            num_factorial *= i
        return num_factorial
    except ValueError:
        return 'Debes ingresar un numero entero positivo valido'
    except AssertionError:
        return 'Debes ingresar un numero positivo'
    
factorial(5)