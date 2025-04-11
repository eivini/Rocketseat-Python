### Declaração
# É possivel fazer declarações com aspas simples e duplas, mas por padrão o ideal é sempre usar aspas duplas "" {
nome_completo = "Marcus Vinícius"

nome_completo_aspas = """"
Marcus
Vinícius"""

nome_completo_quebra = "Marcus \
Vinícius"

nome = "Marcus"
sobrenome = "Vinícius"
# }

### Formatações {
print("Nome completo (1a forma):", nome_completo) # concatenação com o uso de espaço automático
print("Nome completo (2a forma):" + nome_completo) # concatenação sem o uso de espaço automático
print("Nome completo (3a forma):" + "Marcus " + "Vinícius") # concatenação com o uso de + e com espaço no final da primeira string
print("Nome completo (4a forma):" + "Marcus", "Vinícius") # concatenação com o uso de + e o uso de ,
print("Nome completo (5a forma):", nome_completo_aspas)
print("Nome completo (6a forma):", nome_completo_quebra)
print("Nome completo (7a forma): %s" % nome_completo) # concatenação com substituição
print("Nome completo (8a forma): %s %s" % (nome, sobrenome)) # concatenação com mais de uma variável "%s %s" % é necessário passar os valores em ()
print(f"Nome completo (9a forma): {nome} {sobrenome}") # concatenação com format, por padrão colocar o f no início e {} nas variáveis
print("Nome completo (10a forma): {} {}".format(nome, sobrenome)) # essa concatenação funciona na mesma forma que a 9a, mas você ira passar as variáveis depois
"""
Observações sobre concatenações duplas ou mais 
"%s %s" % () é mais segura para tratar os dados
f"{} {}" é visivelmente mais agradável
Valido resaltar: é de extrema importancia usar nomes em variáveis que façam sentido
"""
# }

### Metodos de transformação em upper e lower, caso já tenha uma variável do tipo String {
# Lembrando que as variáveis são imutáveis, apesar do metodo estar mostrando os dados em upper ou lower, o valor dela não é alterado
# .upper
print(".upper",nome.upper())
# .lower
print(".lower",nome.lower())
# é possível percorrer no valor da variável pelo uso dos []
print("Primeiro valor da variável:", nome[0])
print("Segundo valor da variável:", nome[1])
# Vale ressaltar que sempre começamos a contar pelo 0 e não pelo 1
print("Contagem com de 'i' repetidos na variável nome_completo: 'Marcus Vinícius' utilizando o método .find =", nome_completo.count("i"))
print("Retornando o índice/número da primeira vez que aparece a letra 'i' utilizando o método .find", nome_completo.find("i"))
## Metodos de codificação, para conversão de string para bytes
# uma forma mais segura de se trabalhar com strings (existe alguns programas que exigem que trabalhe com bytes)
print("Codificação de string => bytes:", nome.encode()) # codificação de string para bytes
print("Decodificação de bytes => string:", nome.encode().decode()) # decodificação de algo que está em bytes para string
## Metodo replace, ele faz a substituição de uma string por outra
print("Metodo replace fazendo a substituição da letra 'i' para a letra 'e' no nome_completo:", nome_completo.replace("i", "e"))
## Observação: a letra í não foi alterada pela letra e
## Muito utilizada para tratamento de dados, exemplo:
telefone = '(19) 97325-0502'
print("Telefone em string de exemplo para o tratamento de dado:", telefone)
print("Resultado do tratamento para remover o ( :", telefone.replace("(", ""))
# Caso queira fazer mais de uma substituição é necessário fazer outras concatenações
print("Resultado do tratamento para remover tudo que não seja número:", telefone.replace("(", "").replace(")", "").replace(" ", "").replace("-", ""))
# Observação: caso tente remover alguma letra/número/caractere que não existe na string, nada vai acontecer
# }

## Funções join e split, utilizado para conversão de string para listas {
print("Utilização do join:", "-".join(nome))
print("Utilização do join:", "-".join(nome_completo))
print("Utilização do split:", nome_completo.split(" ")) # Caso seja um espaço, não é necessário declarar o espaço (""). Pois o espaço é o parametro default
# }

## Metodos de tratamento de variável strip e (tratamento de textos que tenham ruídos) {
nome_strip = "xMarcus Viníciusx"
print("Utilização do .strip",nome_strip.strip("x")) # ele vai remover a letra/caractere que estiver no início e final
print("Utilização do .rstrip",nome_strip.rstrip("x")) # ele vai remover a letra/caractere do lado direito
# }

## Comparadores in, not in, startswith {
print("Comparação com .startswith: se o nome_completo começa com 'Ma':", nome_completo.startswith("Ma")) # startswith vai sempre te retornar True/False (boolean)
print("Comparação com .startswith: se o nome_completo começa com 'Vi':", nome_completo.startswith("Vi"))
print("Uso de in: em 'us' para o nome_completo:", "us" in nome_completo)
print("Uso de not in: em 'abc' para o nome_completo:", "abc" not in nome_completo)
# }

"""
Não é possível alterar o valor de uma variável
nome[0] = "Josevaldo"
print(nome)
Traceback (most recent call last):
  File "/workspaces/Rocketseat/Python/Nível 1/Modulo_1/tipos_variaveis/texto.py", line 41, in <module>
    nome[0] = "Josevaldo"
    ~~~~^^^
TypeError: 'str' object does not support item assignment
"""