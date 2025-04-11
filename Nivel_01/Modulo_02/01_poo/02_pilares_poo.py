# Os quatro pilares de POO: Abstração, Encapsulamento, Herança e Polimorfismo

# Exemplo de herança
print("Exemplo de herança:")


class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def andar(self):
        print(f"O animal {self.nome} andou")

    # Método genérico, será implementado pelas subclasses
    def emitir_som(self):
        pass


# A classe filha herda da classe mãe
class Cachorro(Animal):
    # Polimorfismo: comportamento diferente para o mesmo método
    def emitir_som(self):
        return "Au, au"


class Gato(Animal):
    def emitir_som(self):
        return "Meow!"


# Polimorfismo em ação
print("\nExemplo de polimorfismo:\n")

dog = Cachorro(nome="Scooby")
cat = Gato(nome="Naru")

animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")


# Encapsulamento: segurança dos dados
print("\nExemplo de encapsulamento:")


class ContaBancaria:
    def __init__(self, saldo) -> None:
        # Atributo privado: só acessível dentro da classe
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo


conta = ContaBancaria(saldo=1000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

conta.depositar(500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

conta.depositar(-500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

conta.sacar(200)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

conta_do_zezinho = ContaBancaria(saldo=50)
print(f"Saldo da conta do Zezinho: {conta_do_zezinho.consultar_saldo()}")


# Abstração: modelo base que outras classes seguem
print("\nExemplo de abstração:")

from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass


class Carro(Veiculo):
    def __init__(self) -> None:
        pass

    def ligar(self):
        return "Carro ligado usando a chave"

    def desligar(self):
        return "Carro desligado usando a chave"


carro_amarelo = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())

# Dica:
# Classes abstratas são muito úteis para acesso ao banco de dados.
# Assim, se um dia o banco mudar, você só precisa adaptar o retorno para seguir o mesmo "contrato" da classe abstrata.
