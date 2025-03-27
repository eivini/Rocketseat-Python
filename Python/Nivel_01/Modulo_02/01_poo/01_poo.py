# Essas linguagens de programação Python, Java, C++, C#, etc, oferecem suporte nativo a programação orientada a objeto
# Permitem que os programadores criem softwer's de maneira modular, reutilizável e mais fácil de se entender
# Programação Orientada a Objetos (POO) = É um paradigma de programação que se baseia na organização dos programas em torno de objetos

# Objetos = Instancias de classes

# Classe exemplo:
# OBS: dentro das classes é possível descrever atributos que são basicamente propriedades dessas classes e seus métodos (ações/oque esses objetos poderam fazer)
# Primeiro método de criação/construtor __init__, ele é como se fosse uma função, mas quando está dentro de uma classe, refere-se a ele como método
# ps: é um método padrão: toda classe vai ter esse método, sempre vai ser esse nome e nunca vai mudar
# (self) = ele é um referência a sua própria classe // uma porta de acesso para que possa utilizar os métodos e atributos dessa classe
# -> None = não é obrigatória a ser usada, mas por padrão as pessoas colocam, mas ela define que esse método não tem retorno
# OBS²: no conceito de objeto não faz sentido deixar algo fixo, como nome, etc.
class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome;
        self.idade = idade;

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.";

# Objetos: é uma instance dessa classe // ele é criado a partir da classe, então ele respeita os atributos e os métodos que a classe tem
# ps: Os atributos são os dados dessa estrutura e os métodos são as funções que a classe pode ter
pessoa1 = Pessoa("Marcus", 27);
# Como não tem nenhum argumento, não é necessário passar nada, pois o self já é uma referencia a ele mesmo
# por estar usando pessoa1 ele já consegue se identificar e ter acesso a seus próprios atributos
mensagem = pessoa1.saudacao();
print(mensagem)

# Ambos os objetos respeitam a estrutura de objetos e tendo os mesmos métodos
pessoa2 = Pessoa(nome="Vinícius", idade=27);
mensagem = pessoa2.saudacao();
print(mensagem)

# Vantagens: reutilização de classes/códigos, organização
# Desvantagens: complexidade (é bastante trabalhoso), curva de aprendizado (prática)
# através da complexidade ele vai ter uma organização e reutilização do código muito melhor, proteção de suas propriedades
# reutilização de classes atraves de heranças, etc.

# Os quatro pilares do POO: encapsulamento, herança, polimorfismo e a abstração
# tudo isso contribui muito para o uso e reutilização dos códigos