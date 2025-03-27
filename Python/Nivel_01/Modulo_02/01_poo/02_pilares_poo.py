# Os quatro pilares de POO: Abstração, Emcapsulamento, Herança e Polimorfismo

# Exemplo de herança
print("Exemplo de herança:")
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome;

    def andar(self):
        print("O animal {self.nome} andou");
        return
    
    # pass, para não deixar vazio ele deixar passar a função
    def emitir_som(self):
        pass

# Herança: a classe filha herda da classe mãe (Classe mãe: Principal, Classe filho: subClasses)
class Cachorro(Animal):
    # é possível alterar o som / comportamento da classe de cima (pelo polimorfismo)
    def emitir_som(self):
        return "Au, au";
    
class Gato(Animal):
    def emitir_som(self):
        return "Meow!";

# Polimorfismo: ajuda a utilizar um método definido pela classe mãe, mas re-implementado de outra forma
# pois ele não precisa se preocupar pois utiliza a mesma estrutura, é o mesmo nome/métodos com implementações diferentes

dog = Cachorro(nome="Scooby");
cat = Gato(nome="Naru");

print("Exemplo de polimorfismo:\n");
animais = [dog, cat];

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}");

# Encapsulamento: segurança desses dados
print("\nExemplo de encapsulamento:");
class ContaBancaria:
    def __init__(self, saldo) -> None:
        # para atribuir um atributo privado, você coloca dois _ => __ , apenas os métodos definidos dentro dessa classe tem acesso a esses dados
        self.__saldo = saldo # Atributo privado
        # ps: não é possível usar o polimorfismo com atributos privados, pois estão fora da classe

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor;
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor;
    
    def consultar_saldo(self):
        return self.__saldo
    
conta = ContaBancaria(saldo=1000);
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor=500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor=-500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.sacar(valor=200)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

conta_do_zezinho = ContaBancaria(saldo=50)
print(f"Saldo da conta do zezinho: {conta_do_zezinho.consultar_saldo()}")

# Abstração: uma classe abstrata não tem a capacidade de se criar objetos atráves dela, não é possível criar uma instância de uma classe abstrata
# ela serve para um molde para outras classes 
# !! vai ajudar a proteger as caracteristicas que os atributos e métodos que uma classe tem que respeitar quando for criada

print("\nExemplo de abstração:")
from abc import ABC, abstractmethod

class Veiculo(ABC):

    @abstractmethod # para definir que é uma classe abstrata
    # no abstractmethod sou obrigado a definir o que essa classe ligar faz
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self) -> None:
        pass

    def ligar(self):
        # Ligação especifica do carro
        return "Carro ligado usando a chave"
    
    def desligar(self):
        return "Carro desligado usando a chave"

carro_amarelo = Carro();
print(carro_amarelo.ligar());
print(carro_amarelo.desligar());

# Todos os métodos com abstractmethod tem que ser respeitado

# Dica: Utilizar classes abstratas para acessar o banco de dados
# em caso de alteração do banco, só precisaria que o retorno do banco novo seja da mesma forma do banco antigo
# porque seu código não necessariamente precisa saber qual banco você está usando, apenas que você tem os métodos 
# Ex: [recuperar dados do banco, deletar dados do banco]