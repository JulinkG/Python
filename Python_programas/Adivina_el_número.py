from random import randint

intentos = 0
numero_secreto = randint(1,100)
nombre = input("Escriba su nombre: ")

print(f"{nombre}, tienes 8 intentos para adivinar el número en el que estoy pensando\n Si lo logras...")

while intentos < 8:
    numero_estimado = int(input("¿En qué número estoy pensando?"))
    intentos += 1

    if numero_estimado < numero_secreto:
        print("El número es mayor")
    
    if numero_estimado > numero_secreto:
        print("El número es menor")

    if numero_estimado == numero_secreto:
        print(f"FELICIDADES {nombre}! Has adivinado en {intentos}, intentos")
        break

if numero_estimado != numero_secreto:
    print(f"Tus intentos se han agotado, el número era {numero_secreto}")