def palabraSinRepeticones(palabra):
    palabraNueva = ""
    for letra in palabra:
        if letra not in palabraNueva:
            palabraNueva += letra
    return palabraNueva

def organizarPalabra(palabra):
    palabraOrdenada="".join(sorted(palabra))
    return palabraOrdenada

def palabraOrganizada(palabra):
    palabraIncial = palabraSinRepeticones(palabra)
    palabraFinal = organizarPalabra(palabraIncial)
    return palabraFinal

palabraTeclado = input("Ingrese una palabra: ")
print(palabraSinRepeticones(palabraTeclado))
print(palabraOrganizada(palabraTeclado))