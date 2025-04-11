# Inteiro {
numero_inteiro = 3
print("Inteiro = ", numero_inteiro)
# }

# Real com ponto flutuante {
numero_real = 3.14
print("Real com ponto flutuante = ", numero_real)
# }

# type() {
print("Tipo da variável inteiro = ", type(numero_inteiro))
print("Tipo da variável real = ", type(numero_real))
# }

# Soma + {
soma = 1 + 1
print("1 + 1 = ", soma)
# }

# Subtração = {
subtracao = 1 - 1
print("1 - 1 = ", subtracao)
# }

# Multiplicação * {
multiplicacao = 2 * 2
print("2 x 2 = ", multiplicacao)
# }

# Divisão / {
# Sempre que for utilizado a divisão, vai ser transformado para float
divisao1 = 4 / 2
divisao2 = 7 / 2 
print("4 / 2 = ", divisao1)
print("Tipo de variável do resultado da divisão = ", type(divisao1))
print("7 / 2 = ", divisao2)
print("Tipo de variável do resultado da divisão = ", type(divisao2))
# }

# Transformações de variáveis {
# Para ter um valor inteiro, é necessário fazer a conversão
# float() => int()
print("Valor inteiro = ", int(divisao1))
print("Valor inteiro = ", int(divisao2))
# Para que um valor inteiro transforme em float, em casos de soma
# int() => float()
print("Valor em float = ", float(soma))
# }

# Resto da divisão {
# Modulo %
modulo = 5 % 2
print("Modulo = ", modulo)
# Divisão inteiro
divisao_inteiro = 5 // 2
print("Divisão inteiro = ", divisao_inteiro)
print("Tipo de variável do resultado da divisão inteiro = ", type(divisao_inteiro))
# }