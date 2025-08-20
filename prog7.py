# Programa 7 – Impressão de Ímpares
n = int(input("Digite um número N: "))

print("Números ímpares entre 1 e", n, ":")
for i in range(1, n + 1):
    if i % 2 == 0:
        continue
    print(i, end=" ")