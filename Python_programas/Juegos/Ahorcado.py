from random import choice

palabras = ['dinosaurio','camaron','desastre','califragilistico','espiralidoso', 'futifantastico','estrategia','pachuco','valheim','jueguitos']
letras_correctas = []
letras_incorrectas = []
vidas = 6
aciertos = 0
juego_terminado = False

def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))

    return palabra_elegida, letras_unicas

def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not es_valida:
        letra_elegida = input("Elige una letra:").lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("No has elegido una letra correcta")

    return letra_elegida

def mostrar_nuevo_tablero(palabra_elegida):

    lista_oculta = []

    for letra in palabra_elegida:
        if letra in letras_correctas:
            lista_oculta.append(letra)
        else:
            lista_oculta.append('-')

    print(''.join(lista_oculta))

def revisar_letra(letra_elegida, palabra_oculta, vidas, coincidencias):

    fin = False

    if letra_elegida in palabra_oculta:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1


    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)

    
    return vidas, fin, coincidencias


def perder():
    print("Ya no te quedan vidas, has muerto")
    print("La palabra oculta era " + palabra)

    return True

def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print("Felicidades has adivinado la palabra!!!")

    return True

palabra, letras_unicas = elegir_palabra(palabras)

while not juego_terminado:
    print("\n" + "*" * 19 + "\n")
    mostrar_nuevo_tablero(palabra)
    print("\n")
    print("Letras incorrectas: " + "-".join(letras_incorrectas))
    print(f"Vidas: {vidas}")
    print("\n" + "*" * 19 + "\n")
    letra = pedir_letra()

    vidas, terminado, aciertos = revisar_letra(letra, palabra, vidas, aciertos)

    juego_terminado = terminado

