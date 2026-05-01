# Declaracao de classes
class Gafanhoto:
    """Classe Gafanhoto: Representa um gafanhoto com nome e idade."""
    def __init__(self, nome = "", idade = 0): # Metodo construtor
        # Atributos de instancia
        self.nome = nome
        self.idade = idade

    # Metodos de instancia
    def aniversario(self):
        self.idade += 1
    
    def __str__(self): # Dunder Method para representar o objeto como string
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade."
    
    def __getstate__(self): # Dunder Method para obter o estado do objeto (usado em serialização)
        return f"Estado: nome =  {self.nome}, idade = {self.idade}"
    

# Declaracao de Objetos
g1 = Gafanhoto("Maria", 17)
g1.aniversario()
print(g1.__dict__) # Dunder Attribute para acessar os atributos do objeto como um dicionário
print(g1.__getstate__()) # Dunder Method para obter o estado do objeto (usado em serialização)
print(g1) # Chama o método __str__ para representar o objeto como string
print(g1.__class__) # Dunder Attribute para acessar a classe do objeto
print(g1.__doc__) # Dunder Attribute para acessar a documentação da classe