# Declaracao {
minha_lista = [1, 10, 2, 3, 3, 4, 5, 8, 6, 7, 112]
# }

# exibindo a lista {
print("Minha lista de exemplo:", minha_lista)
# }

# exibindo os elementos {
# minha_lista[0] = "python" ## comentado para o teste do .sort()
print("Minha lista de exemplo:", minha_lista)

print("minha_lista[0]:", minha_lista[0])
print("minha_lista[5]:", minha_lista[5])
print("minha_lista[1:7]:", minha_lista[1:7]) # minha lista fatiada
print("minha_lista[:5]:", minha_lista[:6]) # fatiando do início ate o final, não é necessário indicar o primeiro elemento, exemeplo: [0:6]
print("minha_lista[2:]:", minha_lista[2:]) # fatiando de um inidice determinado sem declarar o elemento final, ele vai percorrer ate o ultimo elemento
# }

## Métodos de lista

# Método append(): Adiciona um elemento ao final da lista {
minha_lista.append(6)
minha_lista.append(7)
print("Após .append(6) e .append(7):", minha_lista)
# }

# Método index {
indice = minha_lista.index(6)
print("Indice do elemento 6:", indice)
# }

# Método insert: Insere um elemento em um indice específico {
minha_lista.insert(2, 10)
print("Após o .insert(2, 10):", minha_lista)
# }

# Método pop: ele remove e retorna o elemento de um índice específico {
elemento_devido = minha_lista.pop(3)
print("Elemento removido:", elemento_devido)
print("Após .pop(3)", minha_lista)
# }

# Método remove: ele remove o primeiro elemento com o valor especificado {
# minha_lista.remove(True) ## comentado para o teste do .sort()
# print("Após .remove(True):", minha_lista) ## comentado para o teste do .sort()
minha_lista.remove(10)
print("Após .remove(10):", minha_lista)
# }

# Método sort: ele vai organizar a lista em ordem crescente {
minha_lista.sort()
print("Após .sort()", minha_lista)
# }

####
# Observação sobre o método .sort()
# ele não aceita que sua lista tenha vários tipos de elementos, por entando não ira funcionar, pois não tem como ordenar elementos diferentes em ordem crescente
# Traceback (most recent call last):
#   File "/workspaces/Rocketseat/Python/Nível 1/Modulo_1/tipos_variaveis/lista.py", line 42, in <module>
#     minha_lista.sort()
# TypeError: '<' not supported between instances of 'int' and 'str'
####