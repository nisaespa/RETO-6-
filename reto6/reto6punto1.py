import math #importar math para el número pi


#función del volumen y el area superficial total (de las dos figuras sumadas)
def calcular_volumen_y_area_superficial_total(radio1, radio2, generatriz, altura):
    volumen_total = ((4 / 3) * math.pi * radio1**3) + ((1 / 3) * math.pi * radio2**2 * altura)  #formula volumen
    area_superficial_total = (4 * math.pi * radio1**2) + (math.pi * radio2 * (generatriz + radio2))  #formula area superficial
    volumen_total_redondeado = round(volumen_total, 2)  #con round para redondear con solo 2 decimales
    area_superficial_total_redondeado = round(area_superficial_total,2)  #con round para redondear con solo 2 decimales
    return (volumen_total_redondeado, area_superficial_total_redondeado) 
  

#función para pedir los valores e imprimir resultado
def volumen_area():
    radio1 = float(input("Ingrese radio de la esfera en centimetros: "))
    radio2 = float(input("Ingrese radio del cono en centimetros: "))
    generatriz = float(input("Ingrese la generatriz del cono en centimetros: "))
    altura = float(input("Ingrese la altura del cono en centimetros: "))
    volumen, area_superficial = calcular_volumen_y_area_superficial_total(radio1, radio2, generatriz, altura)
    print("El volumen es ", volumen, "centimetros cúbicos y el area superficial es ", area_superficial, "centímetros cuadrados")


if __name__ == "__main__":
    volumen_area()