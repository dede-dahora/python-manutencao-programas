# Programa 8 – Validação de Senha
senha_correta = "senha123"

while True:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Acesso liberado")
        break
    else:
        print("Senha incorreta. Tente novamente.")