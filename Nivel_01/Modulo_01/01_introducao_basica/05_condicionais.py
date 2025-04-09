idade = 19
print("Exemplo de comando if: idade = 19")
if idade >= 18:
    print("Você é maior de idade.")

if idade == 19:
    print("Você tem 19 anos.")

if idade <= 18:
    print("Você é menor de idade.")

if idade != 10:
    print("Você não tem 10 anos.")

idade = 10
print("Exemplo de comando else: idade = 10")
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

idade = 17
print("Exemplo de comando else: idade = 17")
if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 12:
    print("Você é um adolescente.")
else:
    print("Você é menor de idade.")

idade = int(input("Quantos anos você tem? "))

mensagem = "Pode tirar a carteira de habilitação" if idade >= 18 else "Você não pode tirar a carteira de habilitação"
print(mensagem)