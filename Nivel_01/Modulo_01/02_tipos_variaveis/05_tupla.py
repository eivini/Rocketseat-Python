# Tupla é uma coleção ordenada e imutável de elementos
# Criando uma tupla de exemplo {
minha_tupla = (1, 2, 2, 3, 4)

print("Minha tupla:", minha_tupla)

print("minha_tupla[0]:", minha_tupla[0])
print("minha_tupla[2]:", minha_tupla[2])
print("minha_tupla[2]:", minha_tupla[-1]) # utilizando o [-1] ele vai te entregar o último elemento
# }

####
# Observações sobre a tupla:
# não é possível alterar o valor dos elementos, na lista isso funcionaria
# minha_tupla[0] = 5
# Traceback (most recent call last):
#   File "/workspaces/Rocketseat/Python/Nível 1/Modulo_1/tipos_variaveis/tupla.py", line 11, in <module>
#     minha_tupla[0] = 5
#     ~~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment
####

# Método count {
contagem = minha_tupla.count(2)
print("Quantidade de vezes que o elemento 2 aparece:", contagem)
# }

# Método index {
indice = minha_tupla.index(3)
print("Indice da primeira ocorrencia do elemento 3:", indice)
# }