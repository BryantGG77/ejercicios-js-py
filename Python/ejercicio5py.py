# Este codigo lo que hace es buscar fechas en formato dd-mm-aaaa y retornarlas como una lista de listas con la metodologia de regex.

import re

def search_dates_of_birth(text):
    # Patrón para buscar fechas en formato dd-mm-aaaa
    pattern = r'\b(\d{1,2})-(\d{1,2})-(\d{4})\b'
    
    # Buscar todas las coincidencias del patrón en el texto
    matches = re.findall(pattern, text)
    
    # Retornar las fechas encontradas como una lista de listas
    return [[day, month, year] for day, month, year in matches]