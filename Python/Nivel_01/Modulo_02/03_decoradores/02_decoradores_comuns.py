# @classemethod
# @staticmethod

class MinhaClasse:
    valor = 10 # Atributo de classe (valor estático)
    def __init__(self, nome) -> None:
        self.nome = nome # Atributo da instância

    # requer uma instância para ser chamado
    def metodo_instancia(self):
        return f"Método de instância chamado para {self.nome} {self.valor}"    # Ele também consegue acessar os atributos da classe atráves do self
    
    @classmethod    # Decorador @classmethod
    def metodo_classe(cls):    # Sempre que usar o decorar é preciso passar o argumento cls
        return f"Método de classe chamado para valor= {cls.valor}"   # Não é possível acessar o .nome
    
    @staticmethod   # Decorador @staticmethod
    # Geralmente muito utilizado em bibliotecas
    def metodo_estatico():  # Ele não recebe nenhum argumento, então ele não tem acesso nem os atributos da instância, nem os atributos da classe
    #porém ele pode executar uma função especifica, ex: dobrar um valor ou algo do tipo
        return "Método estático chamado"


obj = MinhaClasse(nome="Classe Exemplo")
print(obj.metodo_instancia())
# print(MinhaClasse.metodo_instancia()) # Não é possível acessar diretamente da classe
print(MinhaClasse.valor)    # Não é necessário uma instância para acessar um atributo de uma classe
print(MinhaClasse.metodo_classe())  # Utilizando o @classmethod não é necessario uma instância para poder usar os atributos e os metodos, pode-se utilizar a classe direto
# porém é necessário lembrar sempre de adicionar o cls na classe para poder ter acesso a eles
print(MinhaClasse.metodo_estatico())

class Carro:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod    # normalmente é usado para criar instâncias, a partir de propriedades que podem ser: globais ou atráves de parametros
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")    # É a mesma coisa que se eu tivesse a configuração por lista
        # Exemplo:
        # lista_configuracao = configuracao.split(",")
        # marca = lista_configuracao[0]
        # modelo = lista_configuracao[1]
        # ano = lista_configuracao[2]
        return cls(marca, modelo, int(ano))


configuracao1 = "Toyota,Corolla,2022"
carro1 = Carro.criar_carro(configuracao1)
print(f"Marca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}")

class Matematica:

    @staticmethod
    # Alerta: criar muitos métodos estáticos não é um bom sinal de programação
    # Não criar muitos métodos estáticos, criar métodos de instância que façam sentidos
    # Principalmente em classes que não tenham contexto com o método criado, ex: Matematica => criar um método de criar textos
    def somar(a, b):
        return a + b
    
    
print(Matematica.somar(a=10, b=15))