print("Exemplo de importação de um módulo padrão:")
# import math   // importação de toda biblioteca math (não recomendado)
from math import sqrt   # importando algo especifico da biblioteca math (recomendado)

# raiz_quadrada = math.sqrt(25)    // caso importe todo o módulo
raiz_quadrada = sqrt(25)
print(f"A raiz quadrada de 25 é {raiz_quadrada}")

print("\nExemplo de criação e utilização de um módulo personalizado")
# import meu_modulo    // importando o módulo criado
from meu_modulo import saudacao, dobro

# mensagem = meu_modulo.saudacao("Vinícius")    // resultado importando todo módulo
# resultado_dobro = meu_modulo.dobro(5)    // resultado importando todo módulo
mensagem = saudacao("Vinícius")
resultado_dobro = dobro(5)

print(mensagem)
print(f"O dobro de 5 é {resultado_dobro}")