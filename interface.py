import argparse
import math

class CilindroMagnetico:
    def __init__(self, permeabilidade, area_transversal):
        self.permeabilidade = permeabilidade
        self.area_transversal = area_transversal

class BobinaCobre:
    def __init__(self, numero_voltas, distancia, frequencia):
        self.numero_voltas = numero_voltas
        self.distancia = distancia
        self.frequencia = frequencia

    def cortar_material(self, cilindro):
        potencia_campo = self.calcular_potencia_campo(cilindro)
        print(f'Corte simulado com potência de campo: {potencia_campo:.5f} W')  # Ajustando para exibir apenas 5 casas decimais

    def calcular_potencia_campo(self, cilindro):
        potencia_campo = (self.numero_voltas**2 * cilindro.area_transversal * self.frequencia**2) / (2 * self.distancia**2 * cilindro.permeabilidade)
        return potencia_campo

def main():
    parser = argparse.ArgumentParser(description='Simulação de corte com laser')
    parser.add_argument('-v', '--voltas', type=int, help='Número de voltas da bobina')
    parser.add_argument('-d', '--distancia', type=float, help='Distância entre as bobinas (em metros)')
    parser.add_argument('-f', '--frequencia', type=float, help='Frequência do campo magnético (em Hertz)')
    args = parser.parse_args()

    if not all(vars(args).values()):  # Verificando se todos os argumentos foram fornecidos
        parser.error("É necessário fornecer todos os argumentos: -v/--voltas, -d/--distancia, -f/--frequencia")

    # Configuração do cilindro magnético
    cilindro = CilindroMagnetico(4 * math.pi * 1e-7, 0.01 * 0.01)

    # Configuração da bobina de cobre com informações do usuário
    bobina = BobinaCobre(args.voltas, args.distancia, args.frequencia)

    # Simulação de corte
    bobina.cortar_material(cilindro)

if __name__ == "__main__":
    main()
