import customtkinter as ctk
from controller import Controller

class JanelaPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("400x400")

        self.controller = Controller()

        # Entrada
        self.entrada = ctk.CTkEntry(self, placeholder_text="Digite um número")
        self.entrada.pack(pady=20)

        # Label
        self.label_total = ctk.CTkLabel(self, text="Total: 0.0", font=("Arial", 16))
        self.label_total.pack(pady=10)

        self.label_error = ctk.CTkLabel(self, text="", font=("Arial", 16))
        self.label_error.pack(pady=10)

        # Botões
        self.btn_somar = ctk.CTkButton(self, text="+", command=self.acao_somar)
        self.btn_somar.pack(pady=5)

        self.btn_subtrair = ctk.CTkButton(self, text="-", command=self.acao_subtrair)
        self.btn_subtrair.pack(pady=5)

        self.btn_multiplicar = ctk.CTkButton(self, text="X", command=self.acao_multiplicar)
        self.btn_multiplicar.pack(pady=5)

        self.btn_dividir = ctk.CTkButton(self, text="/", command=self.acao_dividir)
        self.btn_dividir.pack(pady=5)

        self.btn_limpar = ctk.CTkButton(
            self,
            fg_color="#FF5733",
            text="Limpar",
            command=self.acao_limpar
        )
        self.btn_limpar.pack(pady=5)

    # MÉTODO CENTRAL
    def executar(self, funcao):
        self.label_error.configure(text="")
        try:
            valor = float(self.entrada.get())
            resultado = funcao(valor)
            self.label_total.configure(text=f"Total: {resultado}")
            self.entrada.delete(0, 'end')
        except ValueError:
            self.label_error.configure(text="Erro: Valor inválido!")

    # AÇÕES
    def acao_somar(self):
        self.executar(self.controller.somar)

    def acao_subtrair(self):
        self.executar(self.controller.subtrair)

    def acao_multiplicar(self):
        self.executar(self.controller.multiplicar)

    def acao_dividir(self):
        self.executar(self.controller.dividir)

    def acao_limpar(self):
        resultado = self.controller.limpar()
        self.label_total.configure(text=f"Total: {resultado}")
        self.label_error.configure(text="")
        self.entrada.delete(0, 'end')


if __name__ == "__main__":
    app = JanelaPrincipal()
    app.mainloop()