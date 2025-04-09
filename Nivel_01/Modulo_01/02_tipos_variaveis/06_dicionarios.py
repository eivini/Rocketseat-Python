pessoa = {"nome": "Marcus Vinícius", "idade": "27", "cidade": "Patos de Minas"}

print("Meu dicionario de exemplo:", pessoa)

print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

pessoa["sobrenome"] = "Alves"
print("Sobrenome:", pessoa["sobrenome"])
print("Meu dicionario de exemplo atualizado:", pessoa)

pessoa["idade"] = 28
print("Idade atualizada:", pessoa["idade"])

del pessoa["sobrenome"]
print("Meu dicionario de exemplo atualizado:", pessoa)

chaves = list(pessoa.keys())
print("Chaves do dicionário:", chaves)
print("Primeira chave:", chaves[0])

valores = list(pessoa.values())
print("Valores do dicionários:", valores)
print("Primeiro valor do dicionário:", valores[0])

itens = list(pessoa.items())
print("Pares chave-valor do dicionário:", itens)
print("Primeiro valor: %s = %s" % (itens[0][0], itens[0][1]))