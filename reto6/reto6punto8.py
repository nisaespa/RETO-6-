# Importamos las funciones del punto 7 
from reto6punto7 import *
# Se definen las variables utilizadas en las funciones, los 5 números
numero_1 = float(input("Escriba un número: "))
numero_2 = float(input("Escriba un número: "))
numero_3 = float(input("Escriba un número: "))
numero_4 = float(input("Escriba un número: "))
numero_5 = float(input("Escriba un número: "))
# Se almacenan las funciones en variables
promedio = calcular_el_promedio(numero_1, numero_2, numero_3, numero_4, numero_5)
mediana = calcular_la_mediana(numero_1, numero_2, numero_3, numero_4, numero_5)
promedio_multiplicativo = calcular_promedio_multiplicativo(numero_1, numero_2, numero_3, numero_4, numero_5)
orden_ascendente = ordenar_numeros_forma_ascendente(numero_1, numero_2, numero_3, numero_4, numero_5)
orden_descendente = ordenar_numeros_forma_descendente(numero_1, numero_2, numero_3, numero_4, numero_5)
potencia = mayor_numero_elevado_al_menor_numero(numero_1, numero_2, numero_3, numero_4, numero_5)
raiz_cubica_al_menor_numero = raiz_cubica_menor_numero(numero_1, numero_2, numero_3, numero_4, numero_5)
# Se imprimen los cálculos de cada cosa
print("---------------------------------------------------------------------------------")
print("El promedio de los 5 números es: " , promedio)
print("---------------------------------------------------------------------------------")
print("La mediana de los 5 números es: " , mediana)
print("---------------------------------------------------------------------------------")
print("El promedio multiplicativo es: " , promedio_multiplicativo)
print("---------------------------------------------------------------------------------")
print("El orden ascendente de los 5 números es: " , orden_ascendente)
print("---------------------------------------------------------------------------------")
print("El orden descendente de los 5 números es: " , orden_descendente)
print("---------------------------------------------------------------------------------")
print("La potencia del mayor número elevado al menor número es: " , potencia)
print("---------------------------------------------------------------------------------")
print("El valor de la raiz cúbica del menor número es: " , raiz_cubica_al_menor_numero)
print("---------------------------------------------------------------------------------")
