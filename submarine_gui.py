import tkinter as tk
from tkinter import ttk, messagebox

class SubmarineGUI:
    def __init__(self, master):
        self.master = master
        master.title("Controle do Submarino Laser")

        self.label_voltas = ttk.Label(master, text="Número de Voltas:")
        self.label_voltas.grid(row=0, column=0, padx=10, pady=5)

        self.entry_voltas = ttk.Entry(master)
        self.entry_voltas.grid(row=0, column=1, padx=10, pady=5)

        self.label_distancia = ttk.Label(master, text="Distância entre Bobinas (m):")
        self.label_distancia.grid(row=1, column=0, padx=10, pady=5)

        self.entry_distancia = ttk.Entry(master)
        self.entry_distancia.grid(row=1, column=1, padx=10, pady=5)

        self.label_frequencia = ttk.Label(master, text="Frequência do Campo Magnético (Hz):")
        self.label_frequencia.grid(row=2, column=0, padx=10, pady=5)

        self.entry_frequencia = ttk.Entry(master)
        self.entry_frequencia.grid(row=2, column=1, padx=10, pady=5)

        self.label_voltagem_entrada = ttk.Label(master, text="Voltagem de Entrada (V):")
        self.label_voltagem_entrada.grid(row=3, column=0, padx=10, pady=5)

        self.entry_voltagem_entrada = ttk.Entry(master)
        self.entry_voltagem_entrada.grid(row=3, column=1, padx=10, pady=5)

        self.button_simular = ttk.Button(master, text="Simular Corte", command=self.simular_corte)
        self.button_simular.grid(row=4, column=0, columnspan=2, pady=10)

        # Rótulo para exibir as informações
        self.info_label = ttk.Label(master, text="")
        self.info_label.grid(row=5, column=0, columnspan=2, pady=10)

    def calcular_forca_magnetica(self, num_voltas, distancia, frequencia, voltagem_entrada):
        # Constante eletromagnética
        k = 8.99e9

        try:
            # Obter valores do usuário e converter para tipos numéricos
            num_voltas = float(num_voltas)
            distancia = float(distancia)
            frequencia = float(frequencia)
            voltagem_entrada = float(voltagem_entrada)

            # Calcular força magnética
            forca_magnetica = (k * num_voltas ** 2) / (distancia ** 4 * frequencia ** 2)

            # Calcular temperatura (apenas um exemplo, substitua pela fórmula real)
            temperatura = forca_magnetica * 0.002  # Ajuste conforme necessário

            # Exemplo de cálculos para tamanho do feixe
            tamanho_do_feixe = num_voltas * distancia

            # Calcular voltagem de saída com base na voltagem de entrada (exemplo simples)
            voltagem_saida = voltagem_entrada * 0.9  # Ajuste conforme necessário

            # Incluir informações sobre voltagem de entrada e voltagem de saída
            info = {
                "forca_magnetica": forca_magnetica,
                "temperatura": temperatura,
                "tamanho_do_feixe": tamanho_do_feixe,
                "voltagem_entrada": voltagem_entrada,
                "voltagem_saida": voltagem_saida,
            }

            return info
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

    def simular_corte(self):
        num_voltas = self.entry_voltas.get()
        distancia = self.entry_distancia.get()
        frequencia = self.entry_frequencia.get()
        voltagem_entrada = self.entry_voltagem_entrada.get()

        try:
            # Calcular as informações com base nas entradas do usuário
            info = self.calcular_forca_magnetica(num_voltas, distancia, frequencia, voltagem_entrada)

            # Atualizar o rótulo com as informações
            self.info_label.config(text=self.formatar_resposta(info))
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

    def formatar_resposta(self, info):
        return f"""Força Magnética Calculada: {info['forca_magnetica']} N
Temperatura Calculada: {info['temperatura']} °C
Tamanho do Feixe: {info['tamanho_do_feixe']} m
Voltagem de Entrada: {info['voltagem_entrada']} V
Voltagem de Saída: {info['voltagem_saida']} V"""

if __name__ == "__main__":
    root = tk.Tk()
    app = SubmarineGUI(root)
    root.mainloop()
