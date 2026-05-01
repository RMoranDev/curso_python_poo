from rich import print
from rich import inspect

class Funcionario:
    # Atributos de classe
    empresa = "Curso em video"
    # Atributos de instancia
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    

    def apresentar(self) -> str:
        return f":handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {self.__class__.empresa}."


#Funcionario.empresa = "Hostnet"

f1 = Funcionario("Pedro", "Administração", "Diretor")
f1.empresa = "Estudonauta"
print(f1.empresa)
#inspect(f1, methods=True, dunder=True)
print(f1.apresentar())
#inspect(f1)

f2 = Funcionario("Carlos", "TI", "Programador")
print(f2.apresentar())
#inspect(f2)

#inspect(Funcionario)