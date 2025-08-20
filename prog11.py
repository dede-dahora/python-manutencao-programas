# Programa 11 – Função Soma
def soma_valores(lista):
    return sum(lista)

numeros = []
for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

resultado = soma_valores(numeros)
print(f"A soma dos valores é: {resultado}")