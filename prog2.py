# Programa 2 – Contador de Números Pares
n = int(input("Digite um número N: "))

print("Números pares entre 1 e", n, ":")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=" ")