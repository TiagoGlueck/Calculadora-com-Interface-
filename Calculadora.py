class Calculadora:
    def __init__(self):
        self.total = 0.0

    def somar(self, valor):
        self.total += valor
        return self.total

    def subtrair(self, valor):
        self.total -= valor
        return self.total
    
    def multiplicar(self, valor):
        self.total *= valor
        return self.total
    
    def dividir(self, valor):
        if(valor==0):
            # Mostra mensagem de erro abaixo do total
            self.label_error.configure(text="Erro: Valor inválido!")
            return valor
        self.total /= valor
        return self.total
    
    
    def limpar(self):
        self.total = 0
        return self.total