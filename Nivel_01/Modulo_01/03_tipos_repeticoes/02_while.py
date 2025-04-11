print("Exemplo de while")
contador = 0
while contador < 5:
    print("Contagem:", contador)
    contador += 1 # vale o mesmo que contador = contador + 1 / também funciona -= para subtração

####
# O break funciona de uma forma similar, apresentaria o mesmo resultado, mas não é recomendado
# contador = 0
# while True:
#     print("Contagem:", contador)
#     contador += 1
#     if contador == 5:
#         break
####

print("Programa finalizado")