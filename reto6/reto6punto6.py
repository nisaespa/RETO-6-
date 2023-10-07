# Función para calcular el número de contagiados
def numero_de_contagiados(C, D):
    contagiados_totales = C * 2**D # Cada día que pasa el número de contagiados se duplica
    return contagiados_totales
# Función para pedir valores e imprimir contagiados a partir de hoy
def contagiados():
    C = int(input("Ingrese el valor de los contagiados actuales por Covid-19: "))
    D = int(input("Ingrese cuantos días a partir de hoy: "))
    contagiados_totales = numero_de_contagiados(C, D)
    print("Los contagiados a partir de hoy serían", contagiados_totales)
if __name__ == '__main__':
    contagiados()




    