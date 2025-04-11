# Linguagens como Python, Java, C++, C# oferecem suporte à Programação Orientada a Objetos (POO).
# Esse paradigma permite desenvolver software de forma modular, reutilizável e mais fácil de manter.

# POO é baseada na organização do código em torno de objetos — que são instâncias de classes.

# Exemplo de classe:
class Pessoa:
    # O método __init__ é o construtor. Ele inicializa os atributos da classe.
    # 'self' é uma referência à instância atual do objeto.
    # O -> None indica que o método não retorna nenhum valor (opcional).
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    # Método da classe que retorna uma saudação personalizada.
    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."


# Criando objetos (instâncias da classe Pessoa)
pessoa1 = Pessoa("Marcus", 27)
mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Pessoa(nome="Vinícius", idade=27)
mensagem = pessoa2.saudacao()
print(mensagem)


# Vantagens da POO:
# - Reutilização de código (ex: herança)
# - Organização e estrutura
# - Proteção dos dados (encapsulamento)

# Desvantagens:
# - Pode ser mais complexa no início
# - Exige mais prática e planejamento

# Os 4 pilares da POO:
# 1. Abstração
# 2. Encapsulamento
# 3. Herança
# 4. Polimorfismo
