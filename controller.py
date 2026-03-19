from calculadora import Calculadora

class Controller:
    def __init__(self):
        self.calc = Calculadora()

    def somar(self, valor):
        return self.calc.somar(valor)

    def subtrair(self, valor):
        return self.calc.subtrair(valor)

    def multiplicar(self, valor):
        return self.calc.multiplicar(valor)

    def dividir(self, valor):
        return self.calc.dividir(valor)

    def limpar(self):
        return self.calc.limpar()