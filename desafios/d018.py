class Churrasco:
    def __init__(self, titulo, quant_pessoas):
        self.titulo = titulo
        self.quant_pessoas = quant_pessoas

    
    def analisar(self):
        print(f"Analisando {self.titulo} com {self.quant_pessoas} convidados")
        quant_carne = 0.4 * self.quant_pessoas
        custo_total = 82.40 * quant_carne
        custo_pessoa = custo_total / self.quant_pessoas
        print(f"Cada participante comerá 0.4Kg e cada Kg custa R$82.40"
              f"\nRecomendo comprar {quant_carne}Kg de carne")
        print(f"O custo total será de R${custo_total:.2f}"
              f"\nCada pessoa pagará R${custo_pessoa:.2f} para participar.")
        

c1 = Churrasco("Churras do Pepe", 15)
c1.analisar()