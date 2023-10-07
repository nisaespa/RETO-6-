# RETO 6 👽
## Funciones 

1. Dado la figura de la imagen, desarrolle:

<div align='center'>
<figure> <img src="https://i.postimg.cc/FRvCmpxx/image.png" alt="" width="400" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

+ Una función matemática para calcular el volumen y el área superficial.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r1`, `r2` y `h`.
+ Revise como utilizar el valor de `pi` usando *import math* y *math.pi*
                                             
```python
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
```
2. Dado la figura de la imagen, desarrolle:

<div align='center'>
<figure> <img src="https://i.postimg.cc/1t4MrzsL/image.png" alt="" width="400" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

+ Una función matemática para calcular el área y el perimetro.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r`, `a` y `b`.
+ Revise como utilizar el valor de `pi` usando *import math* y *math.pi*

```python
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
```

3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

```python
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
```

4. Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a  3300 cada una y H huevos a  350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

```python
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
```

5. Haga un programa que utilice una función para calcular el valor de un préstamo `C` usando interés compuesto del `i` por `n` meses.

```python
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
```

6. El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

```python
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
```

7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
  + El promedio
  + La mediana 
  + El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
  + Ordenar los números de forma ascendente
  + Ordenar los números de forma descendente
  + La potencia del mayor número elevado al menor número
  + La raíz cúbica del menor número

```python
#Función para calcular promedio de 5 números
def calcular_el_promedio(numero_1, numero_2, numero_3, numero_4, numero_5):
  promedio = (numero_1 + numero_2 + numero_3 + numero_4 + numero_5)/5 #formula promedio
  return promedio
#Función para calcular mediana de 5 números
def calcular_la_mediana(numero_1, numero_2, numero_3, numero_4, numero_5): 
  lista_numeros = [numero_1, numero_2, numero_3, numero_4, numero_5]
  lista_numeros_ordenada = sorted(lista_numeros) #sorted ordena en forma ascendente los números de la lista
  return lista_numeros_ordenada[2] #retorna el tercer elemento de la lista
#Función para calcular promedio multiplicativo de 5 números
def calcular_promedio_multiplicativo(numero_1, numero_2, numero_3, numero_4, numero_5):
  promedio_multiplicativo = (numero_1 * numero_2 * numero_3 * numero_4 * numero_5) ** 1/5
  return promedio_multiplicativo
#Función para ordenar números de forma ascendente
def ordenar_numeros_forma_ascendente(numero_1, numero_2, numero_3, numero_4, numero_5):
  lista_numeros = [numero_1, numero_2, numero_3, numero_4, numero_5]
  lista_numeros_ascendente = sorted(lista_numeros) #sorted ordena en forma ascendente los números de la lista
  return lista_numeros_ascendente
#Función para ordenar números de forma descendente
def ordenar_numeros_forma_descendente(numero_1, numero_2, numero_3, numero_4, numero_5):
  lista_numeros = [numero_1, numero_2, numero_3, numero_4, numero_5]
  lista_numeros_descendente = sorted(lista_numeros, reverse=True) #si sorted ordena de forma ascendente, reverse=True hará lo contrario
  return lista_numeros_descendente
#Función para calcular la potencia del mayor número elevado al menor número
def mayor_numero_elevado_al_menor_numero(numero_1, numero_2, numero_3, numero_4, numero_5):
  lista_numeros = [numero_1, numero_2, numero_3, numero_4, numero_5]
  lista_numeros_ordenada = sorted(lista_numeros) #sorted ordena en forma ascendente los números de la lista
  numero_mayor = lista_numeros_ordenada[4] #número mayor
  numero_menor = lista_numeros_ordenada[0] #número menor
  potencia = numero_mayor ** numero_menor #cálculo potencia
  return potencia
#Función para calcular la raiz cubica del menor número
def raiz_cubica_menor_numero(numero_1, numero_2, numero_3, numero_4, numero_5):
  lista_numeros = [numero_1, numero_2, numero_3, numero_4, numero_5]
  lista_numeros_ordenada = sorted(lista_numeros) #sorted ordena en forma ascendente los números de la lista
  numero_menor = lista_numeros_ordenada[0] #menor número
  raiz_menor = numero_menor ** 1/3 #cálculo raiz cúbica para el menor número
  return raiz_menor 
```

8. Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.

```python
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
```

9. Consultar qué es y cómo funciona *pip* en python.

<div align='center'>
<figure> <img src="https://www.telecomhall.net/uploads/db2683/original/2X/9/93768e7290bc8c8473a02561ac4e608642cfbaca.png" alt="" width="300" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

+ PIP (Package Installer for Python) es una herramienta que se utiliza para instalar y administrar paquetes de software en Python. Los paquetes son módulos o bibliotecas de código que contienen funcionalidades específicas que pueden ser utilizadas en proyectos de Python.

+ PIP funciona conectándose a un repositorio en línea llamado Python Package Index (PyPI), donde se encuentran disponibles paquetes de software de Python. Se utiliza para buscar, instalar, actualizar y desinstalar paquetes de Python de manera sencilla.

10. Hacer un listado de módulos populares para python que se puedan instalar con *pip* y consultar cómo instalarlos.

+ NumPy: una biblioteca para realizar cálculos numéricos y operaciones matemáticas de alto rendimiento.
+ Pandas: una biblioteca para el análisis y manipulación de datos.
+ Matplotlib: una biblioteca para crear gráficos y visualizaciones.
+ Requests: una biblioteca para realizar solicitudes HTTP.
+ Django: un framework para el desarrollo web.
+ Flask: un microframework para el desarrollo web.
+ TensorFlow: una biblioteca para el aprendizaje automático y la inteligencia artificial.
