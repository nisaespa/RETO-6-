# Función para calcular la cantidad de carne de las aves
def calcular_cantidad_de_carne(N,M,K):
    # Gallinas (N) pesan 6 kilos, Gallos (M) 7 kilos y Pollitos (K) 1 kilo
    formula_cantidad_de_carne = 6 * N + 7 * M + K # Formula para la cantidad de carne, conociendo el peso de cada ave
    return formula_cantidad_de_carne
# Función para pedir valores e imprimir la cantidad de carne
def cantidad_carne():
    N = int(input("Ingrese la cantidad de gallinas: "))
    M = int(input("Ingrese la cantidad de gallos: "))
    K = int(input("Ingrese la cantidad de pollitos: "))
    carne_aves = calcular_cantidad_de_carne(N,M,K)
    print("La cantidad de carne de las aves en kilos es:", carne_aves, "Kg")
if __name__ == "__main__":
    cantidad_carne()
    
