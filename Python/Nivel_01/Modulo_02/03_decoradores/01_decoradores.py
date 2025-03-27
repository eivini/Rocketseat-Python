# Decorador = é um tipo especial de função que vai permitir modificar ou estender o comportamento de outras funções
# conseguimos adicionar funcionalidade a funções ou métodos que não necessariamente seja necessario a alteração no código original dessa função
# ex: pegar uma função que já existe e alterar o comportamento dela

def meu_decorador(func):
    def wrapper():   # rapper = embrulhar, embrulha uma função para permitir que faça coisas antes ou depois dessa função ser chamada
        print("Antes da função ser chamada")
        func()
        print("Depois da função ser chamada")
    return wrapper

@meu_decorador  # para que o decorador seja executaod, basta colocar o @nome_do_decorador
def minha_funcao():
    print("Minha função foi chamada")

minha_funcao()
# Obs: bastante utilizado para validar se o usuário está logado na plataforma

class MeuDecoradorDeClasse:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self):
        print("Antes da função ser chamada (decorador de classe)")
        self.func()
        print("Depois da função ser chamada (decorador de classe)")
        
@MeuDecoradorDeClasse        
def segunda_funcao():
    print("Segunda função foi chamada")

segunda_funcao()