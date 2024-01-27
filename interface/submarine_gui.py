import tkinter as tk
from tkinter import ttk
import subprocess

class SubmarineGUI:
    def __init__(self, master):
        self.master = master
        master.title("Controle do Submarino Laser")

        self.label_voltas = ttk.Label(master, text="Número de Voltas:")
        self.label_voltas.grid(row=0, column=0)

        self.entry_voltas = ttk.Entry(master)
        self.entry_voltas.grid(row=0, column=1)

        self.label_distancia = ttk.Label(master, text="Distância entre Bobinas (m):")
        self.label_distancia.grid(row=1, column=0)

        self.entry_distancia = ttk.Entry(master)
        self.entry_distancia.grid(row=1, column=1)

        self.label_frequencia = ttk.Label(master, text="Frequência do Campo Magnético (Hz):")
        self.label_frequencia.grid(row=2, column=0)

        self.entry_frequencia = ttk.Entry(master)
        self.entry_frequencia.grid(row=2, column=1)

        self.button_simular = ttk.Button(master, text="Simular Corte", command=self.simular_corte)
        self.button_simular.grid(row=3, column=0, columnspan=2)

    def simular_corte(self):
        num_voltas = self.entry_voltas.get()
        distancia = self.entry_distancia.get()
        frequencia = self.entry_frequencia.get()

        # Chamar o código C++ com os parâmetros da interface
        subprocess.run(["./lasercuttersubmarine.cpp", "--voltas", num_voltas, "--distancia", distancia, "--frequencia", frequencia])

if __name__ == "__main__":
    root = tk.Tk()
    app = SubmarineGUI(root)
    root.mainloop()
