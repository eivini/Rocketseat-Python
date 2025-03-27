# Exemplo
def saudacao(nome):
    print(f"Olá, {nome}")

print("\nChamando a função saudade:")
saudacao("Marcus")
saudacao("Vinícius")

# Função com retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("\nChamando função quadrado:")
resultado_quadrado = quadrado(5)
print("Resultado da função quadrado:", resultado_quadrado)

# Função com multiplos parâmetros
def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print("\nChamando a função soma:")
numero1 = 20
numero2 = 50
resultado_soma = soma(numero1, numero2)
print(f"A soma do número {numero1} e numero {numero2} é: {resultado_soma}")