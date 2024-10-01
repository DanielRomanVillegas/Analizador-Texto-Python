text = input("Ingresa un texto: ")
text = text.lower()
letras = []

letras.append(input("Ingresa un la primera letra: ").lower())
letras.append(input("Ingresa un la segunda letra: ").lower())
letras.append(input("Ingresa un la tercera letra: ").lower())


#¿Cuántas veces aparece cada una de las letras que eligió?
print("\nCantidad de letras".upper())
cantidad_letras1 = text.count(letras[0])
cantidad_letras2 = text.count(letras[1])
cantidad_letras3 = text.count(letras[2])

print(f"Se ha encontrado la letra '{letras[0]}' repetido {cantidad_letras1} veces")
print(f"Se ha encontrado la letra '{letras[1]}' repetido {cantidad_letras2} veces")
print(f"Se ha encontrado la letra '{letras[2]}' repetido {cantidad_letras3} veces")

#Decir al usuario cuántas palabras hay a lo largo de todo el texto
print("\nCantidad de palabras".upper())
cuantas_palabras = text.split()
print(f"Hay {len(cuantas_palabras)} palabras")

#Primera letra del texto y cuál es la última
print("\nPrimera y última letra".upper())
print(f"La primera letra del texto es: {text[0]}")
print(f"La ultima letra del texto es: {text[-1]}")

#El sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de las palabras.
print("\nOrden inverso de las palabras".upper())
cuantas_palabras.reverse()
texto_invertido = ' '.join(cuantas_palabras)
print(f"Texto invertido: '{texto_invertido}'")

#El sistema nos va a decir si la palabra “Python” se encuentra dentro deltexto
print("\n¿La palabra 'Python' se encuentra dentro del texto?".upper())
text_py= "python" in text
dicc_py= {True:"Sí", False:"No"}
print(f"La palabra 'Python' {dicc_py[text_py]} se encuentra dentro del texto")