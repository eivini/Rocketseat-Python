print("Exemplo de captura de exeções")
try:
    numero = int(input("Digite um número inteiro: ")) # necessário fazer a conversão para inteiro
    resultado = 10 / numero
except ValueError as e:
    print(f"Erro de value error: {e}")
    raise ValueError("Tipo de variaveis incompativeis")
except Exception as e:
    print(f"Erro: {e}")
else:
    print(f"Resultado {resultado}")
finally:
    print("Operação finalizada")

"""
Teste de número sem transformar em inteiro
Erro de divisão de numero e texto 
Traceback (most recent call last):
  File "/workspaces/Rocketseat/Python/Nível 1/Modulo_1/excecoes.py", line 3, in <module>
    resultado = 10 / numero
                ~~~^~~~~~~~
TypeError: unsupported operand type(s) for /: 'int' and 'str'
"""

"""
Teste com uma letra
Erro de transformação de a para inteiro
Traceback (most recent call last):
  File "/workspaces/Rocketseat/Python/Nível 1/Modulo_1/excecoes.py", line 2, in <module>
    numero = int(input("Digite um número inteiro: ")) # necessário fazer a conversão para inteiro
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'a'
"""