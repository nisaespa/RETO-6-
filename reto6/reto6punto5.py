# Función para calcular el valor total del prestamo
def prestamo_con_intereses(C, n, i):
    valor_total_del_prestamo = C * ((1 + i) ** n) # Formula del interés compuesto
    return valor_total_del_prestamo


# Función para pedir valores e imprimir resultado
def valor_prestamo_con_intereses():
    C = float(input("Ingrese el valor del prestamo: "))
    n = int(input("Ingrese en cuantos meses se va a pagar el prestamo: ")) #En valor entero los meses
    i = float(input("Ingrese el valor del interés: "))
    valor_total_del_prestamoo = prestamo_con_intereses(C, n, i)
    print(valor_total_del_prestamoo)

if __name__ == "__main__":
    valor_prestamo_con_intereses()

