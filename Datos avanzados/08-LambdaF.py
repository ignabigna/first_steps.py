usuarios = [["messi", 4],
["Neymar", 8],
["Pulga R", 10]]

def ordena(elemento):
    return elemento[1]

usuarios.sort(key= ordena)
print(usuarios)