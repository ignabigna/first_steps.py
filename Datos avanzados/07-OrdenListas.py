numeros = [1,6, 13, 18, 2, 3, 4, 5, 6, 7, 8]

numeros.sort()
print(numeros)

numeros.sort(reverse = True)
print(numeros)

numeros2 = sorted(numeros)
print(numeros2)

usuarios = [["messi", 4],
["Neymar", 8],
["Pulga R", 10]]

def ordena(elemento):
    return elemento[1]

usuarios.sort(key= ordena)
print(usuarios)
