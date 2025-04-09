class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

pessoa1 = Pessoa("Marcus", 27)

mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Pessoa(nome="Vinícius", idade=27)
mensagem = pessoa2.saudacao()
print(mensagem)