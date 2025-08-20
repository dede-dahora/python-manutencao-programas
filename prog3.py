# Programa 3 – Caixa Eletrônico
valor = int(input("Digite o valor: "))

notas100 = valor // 100
valor = valor % 100

notas50 = valor // 50
valor = valor % 50

notas20 = valor // 20
valor = valor % 20

notas10 = valor // 10

resultado = []
if notas100 > 0:
    resultado.append(f"{notas100} notas de 100")
if notas50 > 0:
    resultado.append(f"{notas50} notas de 50")
if notas20 > 0:
    resultado.append(f"{notas20} notas de 20")
if notas10 > 0:
    resultado.append(f"{notas10} notas de 10")

print(" + ".join(resultado))