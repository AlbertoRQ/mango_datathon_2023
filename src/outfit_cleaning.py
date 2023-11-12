import re

def replace_codes(mapping_dict, codes_list):
    return [mapping_dict.get(code, code) for code in codes_list]

def contiene_numeros(lista):
    # Verificar si algún elemento de la lista contiene números
    return any(re.search(r'\d', elemento) for elemento in lista)


def tiene_mas_de_dos(lista, elementos):
    # Contar la frecuencia de cada elemento en la lista
    conteo = {elemento: lista.count(elemento) for elemento in elementos}
    # Verificar si algún elemento aparece más de dos veces
    return any(cantidad > 1 for cantidad in conteo.values())

def cumple_condiciones(lista):
    lista1 = ["Jeans", "Skirts and shorts", "Trousers & leggings"]
    lista2 = ["Shirts", "Sweaters and Cardigans", "Tops", "T-shirts"]
    cuenta_lista1 = sum(item in lista1 for item in lista)
    cuenta_lista2 = sum(item in lista2 for item in lista)
    tiene_dresses_jumpsuits = "Dresses and jumpsuits" in lista
    return ((cuenta_lista1 == 1 and cuenta_lista2 == 1) or tiene_dresses_jumpsuits)