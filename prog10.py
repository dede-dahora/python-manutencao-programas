# Programa 10 – Acumulador de Valores
soma = 0

while True:
    valor = float(input("Digite um valor (0 para sair): "))
    if valor == 0:
        break
    soma += valor

print(f"Soma total dos valores: {soma}")