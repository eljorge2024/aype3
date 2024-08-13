# cadena de texto simple
'string'
"string" 
# cadena de texto triple
nombre= """tus datos son:
         nombre:jorge
         apellido: hernandez"""

'''tus datos son:
     nombre: jorge
     apellido: hernandez'''
     
print(nombre) # muestra en pantalla lo que esta en la variable nombre
#variables 
a=5
b=8
c=a+b
print(c)
# concatenacion de solo texto 
apellido="jorge"
bienvenido="hola " +apellido +" ¿como estas?"
print(bienvenido) 

# concatenacion que toma un dato y lo convierte a texto 
apellido="5"
bienvenido= f"hola {apellido}  ¿como estas?"
print(bienvenido) 

# del con esto se borra 
apellid="5"
#del apellid
bienvenid= f"hola {apellid}  ¿como estas?"
print(bienvenid) 

# operadores de pertenencias
pais="colombia"
resultado=f"Hola {pais} ¿como estas?"
print("jorge" in resultado)


# definiendo una variable con camelCase
nombreCompleto="jorge luis "

#definicion de una variable con snake_case 
nombre_completo='jorge luis'

# datos compuestos 
# creando lista

# las listas se pueden modificar 
lista= [' jorge hernandez',"soy jorge", True,1.70]
# lo que se encuentra dentro  de corchete [] es el indice de lo que nos va a mostrar 
print(lista[1])

# creando tupla
# las tuplas no se pueden modificar 
tupla=('jorge hernandez', 'soy hernandez',True,1.75)
print(tupla[0])
 
#creando conjunto (set) no muestra datos que esten duplicados(repetidos )
# no se pueden aceder a elementos por indice
conjunto={'jorge guzman', "soy guzman",False,2,False}
print(conjunto)

#creando un diccionario, la estructura es (key : value y separamos con comas) al ultimo elemento no se le pone coma 

diccionario={
    'nombre' : "jorge luis",
    'apellido': "guzman",
    'me gusta programar': True,
    'altura': 1.70
}
# asi se llama a lo que se encuentra en el diccionario
print(diccionario['nombre'])


