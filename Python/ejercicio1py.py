# Este ejercicio lo que hace es iterar sobre las columnas, iterando sobre las filas en cada columna, y comprobar si el valor es 1 (representando un topo) para devolver la ubicación del topo.



def encuetra_el_topo(cajon):
    for columna in range(len(cajon)):  # Iterar sobre las columnas
        for lugar in range(len(cajon[columna])):  # Iterar sobre las filas en cada columna
            if cajon[columna][lugar] == 1:  # Comprobar si el valor es negativo (representando un topo)
                return f'The mole is in row {columna + 1} box {lugar + 1}.'
            
encuetra_el_topo([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]])

# En este caso devolvera 'The mole is in row 6 box 10.'