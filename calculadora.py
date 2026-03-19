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
        if valor == 0:
            raise ValueError("Divisão por zero")
        self.total /= valor
        return self.total

    def limpar(self):
        self.total = 0.0
        return self.total