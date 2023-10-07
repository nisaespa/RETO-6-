import math #importar math para el número pi

# función para hallar el perímetro y el area
def calcular_perimetro_area(lado_a,lado_b,radio):
    perimetro = (2*lado_a)+(2*lado_b) + 2*radio*math.pi #formula perímetro
    perimetro_redondeado = round(perimetro, 2) #con round para redondear con solo 2 decimales
    area = (radio**2)*math.pi+(lado_a*lado_b) #formula área
    area_redondeado = round(area, 2) #con round para redondear con solo 2 decimales
    return (perimetro_redondeado, area_redondeado)

# función para pedir valores e imprimir resultado
def perimetro_area():
    lado_a=float(input("Ingrese cuanto mide el lado a: "))
    lado_b=float(input("Ingrese cuanto mide el lado b: "))
    radio=float(input("Ingrese cuanto mide el radio: "))
    perimetroo, areaa = calcular_perimetro_area(lado_a,lado_b,radio)
    print("El perimetro es ", perimetroo, "centímetros y el área es ", areaa , "centímetros cuadrados")
     

if __name__ == "__main__":
    perimetro_area()



