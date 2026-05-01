class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        print (f"{self.nome:^30}")
        print ("-" * 30)
        print (f"{self.preco:^30}")

p1 = Produto("Iphone 17 Pro Max", 10000)
p1.etiqueta()