import customtkinter as ctk
from Calculadora import Calculadora

class JanelaPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("400x400")

        self.minha_calc = Calculadora()

        # Entrada
        self.entrada = ctk.CTkEntry(self, placeholder_text="Digite um número")
        self.entrada.pack(pady=20)

        # Label
        self.label_total = ctk.CTkLabel(self, text="Total: 0.0", font=("Arial", 16))
        self.label_total.pack(pady=10)
        self.label_error = ctk.CTkLabel(self, text="", font=("Arial", 16))
        self.label_error.pack(pady=10)

        # Botão Somar
        self.btn_somar = ctk.CTkButton(
            self,
            text="Somar",
            command=lambda: self.executar_operacao(self.minha_calc.somar)
        )
        self.btn_somar.pack(pady=5)

        # Botão Subtrair
        self.btn_subtrair = ctk.CTkButton(
            self,
            text="Subtrair",
            command=lambda: self.executar_operacao(self.minha_calc.subtrair)
        )
        self.btn_subtrair.pack(pady=5)

        # Botão Multiplicar
        self.btn_multiplicar = ctk.CTkButton(
            self,
            text="Multiplicar",
            command=lambda: self.executar_operacao(self.minha_calc.multiplicar)
        )
        self.btn_multiplicar.pack(pady=5)

        # Botão Dividir
        self.btn_dividir = ctk.CTkButton(
            self,
            text="Dividir",
            command=lambda: self.executar_operacao(self.minha_calc.dividir)
        )
        self.btn_dividir.pack(pady=5)

        # Botão Limpar
        self.btn_limpar = ctk.CTkButton(
            self,
            fg_color="#FF5733",
            text="Limpar",
            command=self.limpar,
        )
        self.btn_limpar.pack(pady=5)


    def executar_operacao(self, operacao):
        #Limpa mensagem de Erro
        self.label_error.configure(text="")
        try:
            valor = float(self.entrada.get())
            novo_total = operacao(valor)
            self.label_total.configure(text=f"Total: {novo_total}")
            self.entrada.delete(0, 'end')
        except ValueError:
            self.label_error.configure(text="Erro: Valor inválido!")

    def limpar(self):
        novo_total = self.minha_calc.limpar()
        self.label_total.configure(text=f"Total: {novo_total}")
        self.label_error.configure(text="")
        self.entrada.delete(0, 'end')

if __name__ == "__main__":
    app = JanelaPrincipal()
    app.mainloop()