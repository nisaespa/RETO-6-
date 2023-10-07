# Función para el valor de la compra
def compra(P,M,H,B):
    valor_de_la_compra = P * 300 + M * 3300 + H * 350
    return valor_de_la_compra


# Función para pedir valores, calcular vueltas o si se debe, e imprimir resultado
def vueltas_o_debe():
    P = int(input("¿Cuantos panes son?: ")) # En enteros ya que son cosas individuales
    M = int(input("¿Cuantas bolsas de leche son?: "))
    H = int(input("¿Cuantos huevos son?: "))
    B = int(input("¿De qué valor es el billete?: ")) #Los billetes no tienen decimales
    valor_compra = compra(P,M,H,B)
    if B < valor_compra: #Sí falta dinero
        debe = B - valor_compra 
        print("Debe :", debe, "$")
    elif B > valor_compra: #Sí sobró dinero
        vueltas = B - valor_compra
        print("Las vueltas son :", vueltas, "$")
    else: 
        print("No debe, ni hay vueltas")
    
if __name__ == "__main__":
    vueltas_o_debe()




