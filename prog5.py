# Programa 5 – Jogo de Adivinhação
import random

numero_secreto = random.randint(1, 20)

while True:
    palpite = int(input("Adivinhe o número (1-20): "))
    
    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    elif palpite < numero_secreto:
        print("Tente um número maior!")
    else:
        print("Tente um número menor!")