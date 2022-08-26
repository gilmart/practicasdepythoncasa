#comentario con python

#salida por consola
'''
    print("hola mundo")
    print('hola mundo')
'''

#ENTRADAS
#DATOS PRIMITIVOS

from ctypes.wintypes import INT


dato = None
nombre = 'juan'
edad = 33
estatura = 1.62
hincha = True

#SALIDA POR TECLADO
#SE PUEDE CONCATNAR CON + SI TODOS SON STRING/MISMO TIPO DE DATOS
print('hola ', nombre, 'tu edad: ', edad)
print(f'hola {nombre} tu edad es {edad}')

#RECIBIR DATOS POR TECLADO
ciudad=input("digita la ciudad donde vives: ")
print(f'la ciudad donde usted vive es {ciudad}')

#RECIBIR DATOS NUMERICOS POR TECLADO
numero1 = int(input('digita un num1 '))
numero2 = int(input('digita un num2 '))

print(f'el numero 1 es {numero1} y numero 2 es: {numero2}')

#OPERADORS ARITMETICOS - (+-*/%)
