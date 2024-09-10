def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
            
    return nuevo_texto

def reverse(texto):
    texto_reves = ""
    for char in texto:
        texto_reves = char + texto_reves
    return texto_reves

def es_palindromo(texto):
    texto = no_space(texto)
    texto_reves = reverse(texto)
    return texto.lower() == texto_reves.lower()

print(es_palindromo("Amo la paloma"))
print(es_palindromo("amo la falopa"))