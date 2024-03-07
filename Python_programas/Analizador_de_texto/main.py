texto = input("Ingresa un texto a elección: ")
letras = []

texto = texto.lower()

letras.append(input("Ingresa la primeta letra: ").lower())
letras.append(input("Ingresa la segunda letra: ").lower())
letras.append(input("Ingresa la tercera letra: ").lower())

print("\n")
print("CANTIDAD DE LETRAS")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Se ha encontrado la letra {letras[0]} repetida {cantidad_letras1} veces")
print(f"Se ha encontrado la letra {letras[1]} repetida {cantidad_letras2} veces")
print(f"Se ha encontrado la letra {letras[2]} repetida {cantidad_letras3} veces")

print("\n")
print("CANTIDAD DE LETRAS")
palabras = texto.split()
print(f"Se han encontrado {len(palabras)} palabras en el texto")

print("\n")
print("LETRAS DE INICIO Y DE FIN")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La letra inicial es '{letra_inicio}' y la letra final el '{letra_final}'")

print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Si se ordena el texto al revés se obtiene: '{texto_invertido}'")

print("\n")
print("BUSCANDO LA PALABRA PYTHON")
buscar_python = "python" in texto
dic = {True: "Sí", False: "No"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")