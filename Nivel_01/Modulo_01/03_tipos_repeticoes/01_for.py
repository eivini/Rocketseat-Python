print("For utilizando lista")
lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)

print("For utilizando tupla")
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
    print(elemento)

pessoa = {"nome": "Marcus", "idade": 27, "cidade": "Patos de Minas"}
print("\nFor utilizando dicionário - chaves/keys")
for chave in pessoa.keys():
    print(chave)

print("\nFor utilizando dicionário - valores/values")
for valor in pessoa.values():
    print(valor)

print("For utilizando dicionário - itens/items")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

print("\nUtilizando a função range()")
for numero in range(5):
    print("Número:", numero)

print("\nUtilizando a função range() com len()")
lista = [1, 2, 3, 4, 5]
print(lista)
for indice in range(0, len(lista)):
    if indice == 3:
        lista[indice] = 10
    else:
        lista[indice] = 0
    print(lista)

lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")
    if indice == 1:
        print("Indice 1")