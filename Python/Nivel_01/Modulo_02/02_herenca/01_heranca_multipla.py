class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} está amamentando."

class Ave(Animal):
    def voar(self):
        return f"{self.nome} está voando."
    
class Morcego(Mamifero, Ave):
    def emitir_som(self):
        super().emitir_som() # super() é uma função padrão que chama a implementação da classe mãe // não é necessário colocar
        return "Morcegos emitem sons ultrassônicos." 
    
morcego = Morcego(nome="Batman")

# Acessando métodos da classe base 'Animal'
print("Nome do morcego: ", morcego.nome)
# OBS: é possível acessar um dado privado usando _ClassePrincipal __atributoPrivado mas não é recomendado
print("Som do morcego:", morcego.emitir_som())

# Acessando métodos das classes 'Mamiferos' e da classe 'Ave'
print("Morcego amamentando", morcego.amamentar())
print("Morcego voando: ", morcego.voar())