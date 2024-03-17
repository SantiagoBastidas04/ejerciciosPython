from random import *

contadorVidas = 6
nombreUsuario = input("Digita tu nombre... ")
nombreUsuario = nombreUsuario.upper()
print(f"Hola {nombreUsuario} Bienvenido al juego del ahorcado...")

print("Generando Palabra")
listaPalabras = ['sistemas', 'civil', 'automatica']
palabraAleatoria = choice(listaPalabras)
letrasErroneas = [] 
palabraOculta = '_' * len(palabraAleatoria)

def ingresarLetra(letra):
    global contadorVidas, palabraOculta
    if letra in palabraAleatoria:
        print("Letra Encontrada")
        nueva_letra_oculta = ''
        for char,oculta in zip(palabraAleatoria, palabraOculta):
            if char == letra:
                nueva_letra_oculta += char
            else:
                nueva_letra_oculta += oculta
        palabraOculta = nueva_letra_oculta
        print("Palabra Oculta")
        print(palabraOculta)
        if '_' not in palabraOculta:
            print("¡Felicidades! ¡Has adivinado todas las letras!")
            print(f"La palabra Oculta era {palabraAleatoria}")
            return True   
    else:
        contadorVidas -= 1
        print("Letra no encontrada")
        print(f"Vidas Restantes {contadorVidas}")
        letrasErroneas.append(letra)
        print("Letras erróneas:", letrasErroneas)
        if contadorVidas == 0:
            print("¡Has perdido todas tus vidas!")
            return False
    
    

def juego():
    while contadorVidas > 0:
        letra = input("Ingresar letra: ")
        resultado = ingresarLetra(letra)
        if resultado == True:
            break

juego()
               


