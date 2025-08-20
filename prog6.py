# Programa 6 – Busca em Lista
numeros = []
for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

busca = int(input("Digite o número para buscar: "))

encontrado = False
for numero in numeros:
    if numero == busca:
        print("Número encontrado!")
        encontrado = True
        break

if not encontrado:
    print("Número não encontrado")