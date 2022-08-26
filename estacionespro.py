#RETO:
#aceptar palabras mayusculas y minusculas
#estaciones del año con días
#buscar calendario de estaciones
#pedir al usuario mes y dia
#que el programa responda q estacion es
'''
elif(mes != mes and dia != dia ):
    print('el mes que ingreso fue: {mes}, y el dia fue: {dia} intente nuevamente')
'''

mes=input(('Digite el mes: ')).lower()
dia=int(input('Digite el dia: '))

if(mes=='marzo' and dia >20 and dia<=31 or mes=='abril' and dia >=1 and dia<=30 or mes=='mayo' and dia >=1 and dia<=31 or mes=='junio' and dia >=1 and dia<=20 ):
    print(f'el mes es {mes}, el dia es {dia} y la estacion es Primavera')
elif(mes=='junio' and dia >20 and dia<=30 or mes=='julio' and dia >=1 and dia<=30 or mes=='agosto' and dia >=1 and dia<=31 or mes=='septiembre' and dia >=1 and dia<=20 ):
    print(f'el mes es {mes}, el dia es {dia} y la estacion es Verano')
elif(mes=='septiembre' and dia >20 and dia<=30 or mes=='octubre' and dia >=1 and dia<=31 or mes=='noviembre' and dia >=1 and dia<31 or mes=='diciembre' and dia >=1 and dia<=21 ):
    print(f'el mes es {mes}, el dia es {dia} y la estacion es Otoño')
elif(mes=='diciembre' and dia >20 and dia<=31 or mes=='enero' and dia >=1 and dia<=31 or mes=='febrero' and dia >=1 and dia<=28 or mes=='marzo' and dia >=1 and dia<21 ):
    print(f'el mes es {mes}, el dia es {dia} y la estacion es Otoño')  
else:
    print('Error al ingresar los datos, intente nuevamente')
