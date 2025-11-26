main_text = input("Ingrese el texto que desea analizar: ").lower().strip()
strings_to_find = list(input("Ingrese las tres letras que desea buscar en el texto: ").lower())
special_chars = [" ", "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/",":", ";", "<", "=", ">", "?", "@","[", "\\", "]", "^", "_", "`","{", "|", "}", "~"]

#Función que utiliza la lista de caracteres especiales para descartarlos de "strings_to_find".
def discard_chars():
    for string_to_find in range(len(strings_to_find)-1):
        for chars in special_chars:
            if chars in strings_to_find:
                strings_to_find.remove(chars)

discard_chars()

#Revisa que las letras que desea buscar el usuario no pasen de la cantidad de letras indicadas.
while len(strings_to_find) < 3 or len(strings_to_find) > 3:
    strings_to_find = list(input("Debe ingresar tres letras: "))
    discard_chars()

#Le dice al usuario cuantas veces aparecen en el texto las letras que eligió.
main_text_characters = list(main_text)
for i in range(len(strings_to_find)):
    print(f"Veces que aparece '{strings_to_find[i]}' en el texto: {main_text_characters.count(strings_to_find[i])}\n")

#Le dice al usuario cuantras palabras hay en el texto.
main_text_words = main_text.split()
print(f"La cantidad de palabras que hay en el texto son: {len(main_text_words)}\n")

#Le dice al usuario cual es la primera y ultima letra del texto.
print(f"La primera letra del texto es: {main_text_characters[0]} y la ultima letra del texto es: {main_text_characters[-1]}\n")

#Retorna el texto principal invertido.
main_text_reversed = "".join(main_text_characters[::-1])
print(f"El texto a la inversa es:\n{main_text_reversed}\n")

#Decirle al usuario si la palabra python existe en el texto utilizando un diccionario de apoyo.
boolean_response = {True:"Python existe dentro del texto\n", False:"Python no existe dentro del texto\n"}
print(f"{boolean_response["python" in main_text]}")