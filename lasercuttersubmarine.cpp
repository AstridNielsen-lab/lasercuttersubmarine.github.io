#include <iostream>
#include <cmath>
#include <string>
#include <cxxopts.hpp>

class CilindroMagnetico {
public:
    double permeabilidade; // Permeabilidade magnética do material
    double areaTransversal; // Área da seção transversal do cilindro

    CilindroMagnetico(double permeabilidade, double areaTransversal)
        : permeabilidade(permeabilidade), areaTransversal(areaTransversal) {}
};

class BobinaCobre {
public:
    int numeroVoltas;
    double distancia; // Distância entre as bobinas
    double frequencia; // Frequência do campo magnético

    BobinaCobre(int numeroVoltas, double distancia, double frequencia)
        : numeroVoltas(numeroVoltas), distancia(distancia), frequencia(frequencia) {}

    void cortarMaterial(const CilindroMagnetico& cilindro) const {
        double potenciaCampo = calcularPotenciaCampo(cilindro);
        std::cout << "Corte simulado com potência de campo: " << potenciaCampo << " W\n";
    }

private:
    double calcularPotenciaCampo(const CilindroMagnetico& cilindro) const {
        double potenciaCampo = (pow(numeroVoltas, 2) * cilindro.areaTransversal * pow(frequencia, 2))
                               / (2 * pow(distancia, 2) * cilindro.permeabilidade);
        return potenciaCampo;
    }
};

int main(int argc, char* argv[]) {
    cxxopts::Options options("LasercutterSubmarine", "Simulação de corte com laser");

    options.add_options()
        ("v,voltas", "Número de voltas da bobina", cxxopts::value<int>())
        ("d,distancia", "Distância entre as bobinas (em metros)", cxxopts::value<double>())
        ("f,frequencia", "Frequência do campo magnético (em Hertz)", cxxopts::value<double>())
        ;

    auto result = options.parse(argc, argv);

    int numVoltas = result["voltas"].as<int>();
    double distBobinas = result["distancia"].as<double>();
    double freqCampo = result["frequencia"].as<double>();

    // Configuração do cilindro magnético
    CilindroMagnetico cilindro(4 * M_PI * 1e-7, 0.01 * 0.01);

    // Configuração da bobina de cobre com informações do usuário
    BobinaCobre bobina(numVoltas, distBobinas, freqCampo);

    // Simulação de corte
    bobina.cortarMaterial(cilindro);

    return 0;
}
