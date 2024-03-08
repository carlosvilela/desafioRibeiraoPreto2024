# soma dos 2 numeros anteriores

numero_anterior = 1
numero_atual = 1
quantidade = 7

print(numero_anterior)
print(numero_atual)

for _ in range(quantidade):
    proximo_numero = numero_anterior + numero_atual
    print(proximo_numero)
    
    numero_anterior = numero_atual
    numero_atual = proximo_numero
