nome_completo = "Marcus Vinícius"

nome_completo_aspas = """"
Marcus
Vinícius"""

nome_completo_quebra = "Marcus \
Vinícius"

nome = "Marcus"
sobrenome = "Vinícius"

print("Nome completo (1a forma):", nome_completo)
print("Nome completo (2a forma):" + nome_completo)
print("Nome completo (3a forma):" + "Marcus " + "Vinícius")
print("Nome completo (4a forma):" + "Marcus", "Vinícius")
print("Nome completo (5a forma):", nome_completo_aspas)
print("Nome completo (6a forma):", nome_completo_quebra)
print("Nome completo (7a forma): %s" % nome_completo)
print("Nome completo (8a forma): %s %s" % (nome, sobrenome))
print(f"Nome completo (9a forma): {nome} {sobrenome}")
print("Nome completo (10a forma): {} {}".format(nome, sobrenome))
print(".upper",nome.upper())
print(".lower",nome.lower())
print("Primeiro valor da variável:", nome[0])
print("Segundo valor da variável:", nome[1])
print("Contagem com de 'i' repetidos na variável nome_completo: 'Marcus Vinícius' utilizando o método .find =", nome_completo.count("i"))
print("Retornando o índice/número da primeira vez que aparece a letra 'i' utilizando o método .find", nome_completo.find("i"))
print("Codificação de string => bytes:", nome.encode())
print("Decodificação de bytes => string:", nome.encode().decode())
print("Metodo replace fazendo a substituição da letra 'i' para a letra 'e' no nome_completo:", nome_completo.replace("i", "e"))

telefone = '(19) 97325-0502'
print("Telefone em string de exemplo para o tratamento de dado:", telefone)
print("Resultado do tratamento para remover o ( :", telefone.replace("(", ""))
print("Resultado do tratamento para remover tudo que não seja número:", telefone.replace("(", "").replace(")", "").replace(" ", "").replace("-", ""))
print("Utilização do join:", "-".join(nome))
print("Utilização do join:", "-".join(nome_completo))
print("Utilização do split:", nome_completo.split(" "))

nome_strip = "xMarcus Viníciusx"
print("Utilização do .strip",nome_strip.strip("x"))
print("Utilização do .rstrip",nome_strip.rstrip("x"))

print("Comparação com .startswith: se o nome_completo começa com 'Ma':", nome_completo.startswith("Ma"))
print("Comparação com .startswith: se o nome_completo começa com 'Vi':", nome_completo.startswith("Vi"))
print("Uso de in: em 'us' para o nome_completo:", "us" in nome_completo)
print("Uso de not in: em 'abc' para o nome_completo:", "abc" not in nome_completo)