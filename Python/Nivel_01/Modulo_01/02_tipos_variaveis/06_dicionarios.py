## O dicionario no python é uma coleção não ordenada de pares chave/valor
# Criando um dicionario de exemplo {
pessoa = {"nome": "Marcus Vinícius", "idade": "27", "cidade": "Patos de Minas"}
# }

# Exibindo o dicionario {
print("Meu dicionario de exemplo:", pessoa)
# }

# Acessando valores por chave {
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

pessoa["sobrenome"] = "Alves" # É possível adicionar qualquer tipo de valor: int/string/boolean/float, também é possível adicionar outros dicionarios
print("Sobrenome:", pessoa["sobrenome"])
print("Meu dicionario de exemplo atualizado:", pessoa)
####
# Observação: caso tente buscar um valor em uma chave inesistente, vai apresentar o seguinte erro, porém é possível atribuir valores depois de ser instanciado
# Traceback (most recent call last):
#   File "/workspaces/Rocketseat/Python/Nível 1/Modulo_1/tipos_variaveis/dicionarios.py", line 12, in <module>
#     print("Sobrenome:", pessoa["sobrenome"])
#                         ~~~~~~^^^^^^^^^^^^^
# KeyError: 'sobrenome'
####

pessoa["idade"] = 28
print("Idade atualizada:", pessoa["idade"])
# }

# Removendo um par chave-valor (ele exclui tanto a chave quanto o valor dela) {
del pessoa["sobrenome"]
print("Meu dicionario de exemplo atualizado:", pessoa)
# }

# Métodos: keys(), values(), items()

# .keys() {
chaves = list(pessoa.keys()) # transformando em list, será possível mostrar os valores
print("Chaves do dicionário:", chaves) # é possível acessar cada chave dela, como se fosse uma lista
print("Primeira chave:", chaves[0])
# }

####
# Observações sobre o .keys: caso apresente esse erro, é porque o objeto que ele retornou não é uma lista direta
# print("Chaves do dicionário:", chaves)
# Traceback (most recent call last):
#   File "/workspaces/Rocketseat/Python/Nível 1/Modulo_1/tipos_variaveis/dicionarios.py", line 38, in <module>
#     print("Primeira chave:", chaves[0])
#                              ~~~~~~^^^
# TypeError: 'dict_keys' object is not subscriptable
####

# .values() {
valores = list(pessoa.values()) # caso transforme em list, funciona da mesma forma que o .keys()
print("Valores do dicionários:", valores)
print("Primeiro valor do dicionário:", valores[0])
# }

# .items() {
itens = list(pessoa.items())
print("Pares chave-valor do dicionário:", itens)
print("Primeiro valor: %s = %s" % (itens[0][0], itens[0][1])) # sempre tem que colocar dois valores, o valor da tupla e o valor declarado como no exemplo
# }