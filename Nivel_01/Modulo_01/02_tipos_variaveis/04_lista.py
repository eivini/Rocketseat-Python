minha_lista = [1, 10, 2, 3, 3, 4, 5, 8, 6, 7, 112]

print("Minha lista de exemplo:", minha_lista)

print("Minha lista de exemplo:", minha_lista)

print("minha_lista[0]:", minha_lista[0])
print("minha_lista[5]:", minha_lista[5])
print("minha_lista[1:7]:", minha_lista[1:7])
print("minha_lista[:5]:", minha_lista[:6])
print("minha_lista[2:]:", minha_lista[2:])

minha_lista.append(6)
minha_lista.append(7)
print("Após .append(6) e .append(7):", minha_lista)

indice = minha_lista.index(6)
print("Indice do elemento 6:", indice)

minha_lista.insert(2, 10)
print("Após o .insert(2, 10):", minha_lista)

elemento_devido = minha_lista.pop(3)
print("Elemento removido:", elemento_devido)
print("Após .pop(3)", minha_lista)

minha_lista.remove(10)
print("Após .remove(10):", minha_lista)

minha_lista.sort()
print("Após .sort()", minha_lista)