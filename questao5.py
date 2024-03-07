meuNome = input("Digite o seu nome: ")

def inverter(nome):
    resultado = ""
    tamanhoNome = len(nome)
    indice = tamanhoNome - 1

    while indice >= 0:
        resultado += nome[indice]
        indice -= 1

    return resultado

meuNome = inverter(meuNome)
print(f"Nome invertido: {meuNome}")
