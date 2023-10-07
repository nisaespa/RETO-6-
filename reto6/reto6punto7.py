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

