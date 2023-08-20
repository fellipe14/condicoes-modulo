import math

def calcular_latas_tinta(area_parede, rendimento_lata):
    latas_necessarias = math.ceil(area_parede / rendimento_lata)
    return latas_necessarias

def main():
    largura_parede = float(input("Digite a largura da parede em metros: "))
    altura_parede = float(input("Digite a altura da parede em metros: "))
    rendimento_lata = float(input("Digite o rendimento da lata de tinta em metros quadrados por lata: "))

    area_parede = largura_parede * altura_parede
    latas_necessarias = calcular_latas_tinta(area_parede, rendimento_lata)

    print(f"Serão necessárias {latas_necessarias} latas de tinta para pintar a parede.")

if __name__ == "__main__":
    main()
