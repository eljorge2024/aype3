# los operadores arirmeticos 

# suma(+)
#resta(-)
#multiplicacion(*)
#division(/)
#modulo , devuelve el resto de la division
# exponente **
#division baja //

a=10
b=5
#suma
suma=a+b
print(suma)
#resta
resta=a-b
print(resta)
#multiplicacion
multiplicacion=a*b
print(multiplicacion)
#division
division=a/b
print(division)
#potenciacion o exponente
exponente=a**b
print(exponente)
#division baja 
division_baja=a//b
print(division_baja)
#modulo
modulo=a%b
print(modulo)

# operadores de comparacion 
#  ==  es igual que
# != es distinto de 
# < es menor que 
# <= es menor o igual 
# > es mayor que 
# >= es mayo o igual 


igual_que=5==6

distinto_de=5!=9

mayor_que=5>6

mayo_o_igual=5>=6

menor_que=5<6

print(igual_que)


#calculos combinados 
m=10
l=2
p=62
comparacion=m+l<p
print(comparacion)



# condicionales 
ingresos_mensuales=10000
gastos_mensuales=4800
if ingresos_mensuales>5000:
    print("podes sobrevivir ")
    if gastos_mensuales>4500:
      print(" no te da")
  
elif ingresos_mensuales>10000:
    print("estas bien en todas partes")
      
    
else:
    print("no podes pasar")    
    

# AND
# OR
# NOT


cadena1='Hola soy jorge'
cadena2='very good'




# dir funciona para 
print(dir(cadena1))

# upper convierte a mayuscula
mayuscula=cadena1.upper()
print(mayuscula)

# lower convierte a minuscula
minuscula=cadena1.lower()
print(minuscula)

# capitalize primera en mayuscula
primera_en_mayuscula=cadena1.capitalize()
print(primera_en_mayuscula)

# find metodo encuentra la primera aparicion del valor especifico, sino devuelve 1
primero=cadena2.find('y')
print(primero)

# index metodo encuentra la primera aparicion del valor especifico, si no devuelve una excepcion
segundo=cadena2.index('y')
print(segundo)

# isnumeric  si es numerico devuelve tru
numerico=cadena1.isnumeric()
print(numerico)

# isalpha si es alfa numerico devuelve tru
devuelve=cadena1.isalpha()
print(devuelve)

#count devuelve el numero de ocurrencias de una subcadena en la cadena dada
tercer=cadena1.count('a')
print(tercer)

# len cuenta los caracteres de una cadena
cuenta=cadena2.__len__()
print(cuenta)

# endswith verifica si una cadena comienza con lo dado
verifica=cadena1.endswith('h')
print(verifica)

# startswith verifica si una cadena termina con 
very=cadena2.startswith('d')
print(very)

# replace remplaza un valor por otro 
remplaza=cadena2.replace('very', 'happy')
print(remplaza)

# split separa por el parametro dado 
separa=cadena1.split('  ')
print(separa)


#   creando una lista con list()
lista=list(['hola','jorge',18,19,20])
print(lista)
#devuelve la cantidad de elemnetos de la lista
resultado= len(lista)
print(resultado)
#agregando un elemento a la lista con append
lista.append('jojojojo')
print(lista)

#agregando un elemento a la lista en un indice especifico
lista.insert(0,'siuu')
print(lista)

#agregando varios elementos a la lista 
lista.extend([False,2030])
print(lista)

#eliminando un elemento de la lista por su indice 
lista.pop(0)
print(lista)

#removiendo un elemento por su valor
lista.remove('jorge')
print(lista)


#ordenando la lista  que no tenga cadenas de texto
lista1=list(['12','18'])
lista1.sort(reverse=True)
print(lista1)

#invirtiendo los elementos de una lista 
lista1.reverse()
print(lista1)

#eliminado todo los elementos de la lista 
lista.clear()
print(lista)